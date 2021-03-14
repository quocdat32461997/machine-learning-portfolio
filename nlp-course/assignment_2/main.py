"""
Author: Dat Quoc Ngo
Date: March 9, 2021
NET-ID: dqn170000
"""

# import dependencies
import os
import re
import json
import argparse
from functools import reduce
import numpy as np
from collections import defaultdict

def _find_word(input):
	"""
	_find_word - function to find words in the input sentence
	Inputs:
		- input : string
			Input sentence
	Outputs:
		- outputs : list
			List of words
	"""
	# lower case
	input = input.lower()

	# split by whitespace
	input = re.split(pattern = '[\s]+', string = input)

	# find words in WORD_POS pattern
	valid_word = lambda x: True if re.findall(pattern = r'[a-z]*_[a-z]*', string = x) else False
	outputs = []
	for token in input:
		if valid_word(token):
			outputs.append(token.split('_')[0])
	return outputs

def process(input):
	"""
	process - functino for text-processing
	Inputs: 
		input - string
			Input text
	Outputs:
		input - nested list
			List of word-list
	"""

	# split by newline
	input = re.split(pattern = r'\n', string = input)

	# split into tokens by whitespace
	input = [_find_word(sent) for sent in input]

	return input

def compute_unigram(input, unigram_count, total_word):
	"""
	compute_unigram - function to compute unigram probability
	Inputs:
		input : str
			Word
		unigram_count : defaultdict(int)
			Occurence hasmap of words/tokens
		total_word : int
			Total number of words/tokens
	Outputs:
		output : float
			unigram probability
	"""
	return unigram_count[input] / total_word

def compute_bigram(input, unigram_count, bigram_count):
	"""
	compute_bigram - function to compute bigram probability
	Inputs:
		input : tuple
			bigram
		unigram_count : defaultdict(int)
			Occurence hashmap of single words/tokens
		bigram_count : defaultdict(int)
			Occurence hasmap of bi-words/tokens
	Outputs:
		output : float
			Bigram probability
	"""
	return bigram_count[input] / unigram_count[input[0]]

def build_bigram(input):
	"""
	build_bigram - function to build bigram model
	Inputs:
		- input : nested list
			List of words/sentence
	Outputs:
		- unigram_count : defaultdict
			Hashmap of "unigram : frequency"
		- bigram_count : defaultdict
			Hashmap of "bigram : frequency"
		- bigram_prob : defaultdict
			Hashmap of "bigram : bigram probability"
		- bigram_freq : defaultdict
			Hashmap of "frequency : count" to store the count of bigram occurence
		- total_word : int
			Total number of tokens
		- total_vocab : int
			Vocabulary size
	"""
	
	# initialize unigram & bigram
	unigram_count, bigram_count = defaultdict(int), defaultdict(int)
	bigram_prob, bigram_freq = defaultdict(float), defaultdict(int)
	total_word, total_bigram = 0, 0

	# iterate thru tokens
	for sent in input:
		if sent:
			total_word += len(sent)
			total_bigram += len(sent)-1 if len(sent) > 1 else 0
			unigram_count[sent[0]] += 1
			for idx in range(1, len(sent)):
				unigram_count[sent[idx]] += 1
				bigram_count[tuple(sent[idx - 1 :idx + 1])] += 1

	# compute bigram prob and bigram-frequency
	for bigram, count in bigram_count.items():
		bigram_prob[bigram] = compute_bigram(bigram, unigram_count, bigram_count) # bigram prob
		bigram_freq[count] += 1 # count number of bigram-frequency count

	# compute total vocab
	total_vocab = len(unigram_count)

	return unigram_count, bigram_count, bigram_prob, bigram_freq, total_word, total_vocab, total_bigram

def test(input, type, unigram_count, bigram_count, bigram_prob, bigram_freq, total_word, total_vocab, total_bigram):
	"""
	test - function to compute bigram probability of the input sentence
	Inputs:
		input : str
			Sentence
		unigram_count : defaultdict
		bigram_count : defaultdict
		bigram_prob : defaultdict
		bigram_freq : defaultdict
		total_word : int
		total_vocab : int
		total_bigram : int
	Outputs:
		output : float
			Bigram probability
	"""

	def _process_test(input):
		"""
		_process_test : function to process incoming test
		Inputs:
			input : str
		Outputs:
			_ : list of words
		"""

		# split by whitespace
		return re.split(pattern = '\s+', string = input.lower())

	def _compute_bigram_prob(input):
		"""
		_compute_bigram_prob
		Inputs:
			input : list 
				List of tokens
		Outputs:
			output : float
				Bigram probability
		"""
		
		# prob of token_0 a.k.a first token
		outputs = [unigram_count[input[0]] / total_word]

		if type == 'no-smoothing': # no-smoothing
			# compute the remaining bigram probs
			for idx in range(1, len(input)):
				# get bigram
				bigram = tuple(input[idx - 1:idx + 1])

				# compute prob
				outputs.append(bigram_count[bigram] / unigram_count[input[idx - 1]])

				# zero break
				if outputs[-1] == 0:
					print(input[idx], 'not in corpus')
					break
		elif type == 'add-one-smoothing': # add-one-smoothing
			# compute the remaining bigram probs
			for idx in range(1, len(input)):
				# get bigram
				bigram = tuple(input[idx - 1:idx + 1])

				# compute prob
				outputs.append((bigram_count[bigram] + 1) / (unigram_count[input[idx - 1]] + total_vocab))

				if outputs[-1] == 0:
					print(input[idx], 'not in corpus')
					break

		else: # good-turing
			# compute the remaining bigram probs
			for idx in range(1, len(input)):
				# find frequency of bigram
				count = bigram_count[tuple(input[idx - 1:idx + 1])]

				# compute prob
				if count == 0: # bigram not existing in training corpus
					n_count_1 = bigram_freq[count + 1]
					outputs.append(0 if n_count_1 == 0 else n_count_1 / total_bigram) # if N(count+1) == 0, then probability is 0

				else: # defaultdict already handles N_c+1 = -> count* = 0
					outputs.append((count + 1) * bigram_freq[count + 1] / (bigram_freq[count] * total_bigram))

				# zero break
				if outputs[-1] == 0:
					print('Either bucket {} = or {} not in corpus'.format(count + 1, input[idx]))
					break

		return outputs

	print('Computing probability of {}'.format(input))

	# process text
	assert len(input) > 0, 'Length of test input msut be greater than 0'
	input = _process_test(input)

	# compute test probability by bigram model
	assert type in ['no-smoothing', 'add-one-smoothing', 'good-turing'], 'smoothing selection shouuld be no-smoothing, add-one-smoothing, and good-turing'
	outputs = _compute_bigram_prob(input)

	# compute the final output
	output = reduce(lambda x, y: x*y, outputs)
	print('{}: {} = {}'.format(type, ' * '.join([str(x) for x in outputs]), output))

	return None

def main(args):
	# read data corpus
	with open(args.input) as file:
		data = file.read()

	# process text
	data = process(data)

	# compute unigram & bigram model
	unigram_count, bigram_count, bigram_prob, bigram_freq, total_word, total_vocab, total_bigram = build_bigram(data)
	print("Total word {}, total vocabulary {}, total bigram {}".format(total_word, total_vocab, total_bigram))

	# test
	bigram_prob = test(args.test, args.type, unigram_count, bigram_count, bigram_prob, bigram_freq, total_word, total_vocab, total_bigram)

	# save unigram and bigram
	with open('unigram.json', 'w') as file:
		json.dump(unigram_count, file)
	with open('bigram.json', 'w') as file:
		bigram_count = {str(bigram) : count for bigram, count in bigram_count.items()}
		json.dump(bigram_count, file)
	return None

if __name__ == '__main__':
	# initialize parser
	parser = argparse.ArgumentParser()

	# add arugment
	parser.add_argument('--type', type = str, default = 'no-smoothing', help = 'Smoothing type: no-smoothing, add-one-smoothing, and good-turing')
	parser.add_argument('--input', type = str, default = 'NLP6320_POSTaggedTrainingSet-Unix.txt', help = 'Path to input data')
	parser.add_argument('--test', type = str, default = 'test test', help = 'Text for computing probability')

	# execute
	main(parser.parse_args())
