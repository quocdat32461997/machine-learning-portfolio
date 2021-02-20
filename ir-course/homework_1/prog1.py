"""
Author: Dat Quoc Ngo
NET-ID: dqn170000
Date: Feb. 19, 2021
File: main.py - for executing homework 1
"""

# import dependencies
import os
import re
import argparse
from collections import defaultdict

def tokenize(text):
	"""
	tokenize - function to perform tokenization
	Inputs:
		- 
		-
	Outputs:
		- 
	"""
	# substitue puncutations with whitespace
	text = re.sub(pattern = '[.!?\\-<>]*', repl = '', string = text)

	# strip heading, tailing, and in-middle whitepsace
	text = re.sub(pattern = '\s\s+', repl = ' ', string = text)

	# strip heading and taling whitepsace
	text = text.strip()

	# split text into tokens by whitespace
	text = text.split(' ')

	return text

def stem(text):
	"""
	stem - function to stem text
	"""

	return text

def process(text, pattern = '(<\/?[a-zA-Z]*>)|(\n)'):
	"""
	process - process SGML-styled text into preferred text
	Inputs:
		- text : raw text
		- pattern : matching pattern to remove SGML tags
	Outputs:
		- text : processed text
	"""

	# remove SGML tags
	text = re.sub(pattern = pattern, repl = '', string = text)

	return text

def main(args):

	# retrieve list of text files
	files = os.listdir(args.path)
	files = [os.path.join(args.path, x) for x in files]

	# initialize dictionary to store term, its frequency, and positions
	terms = defaultdict(int)

	for file in files:
		# read text
		with open(file) as f:
			text = f.read()
		# process
		text = process(text)
		# tokenization
		tokens = tokenize(text)
		# stemming

		# store terms
		for token in tokens:
			terms[token] += 1

	# print required results
	print("Number of tokens in Cranfield text collections is {}.".format(sum([v for v in terms.values()])))
	print("Number of unique tokens in Cranfield text collections is {}.".format(len(terms)))

	# sort terms by descending frequency
	terms = sorted(terms.items(), key = lambda x : x[-1], reverse = True)

	# print tokens occuring only once
	onces = []
	while terms:
		if terms[-1][-1] == 1: # occuring only once
			onces.append(terms.pop()[0])
		else:
			break # stop

	print("List of words occuring only once: {}".format(onces))
	print("List of 30 most frequent words in the collection: {}".format([x[0] for x in terms[:30]]))

	return None

if __name__ == '__main__':
	# initialize argument parser
	parser = argparse.ArgumentParser(description = 'Argument parser for homework 1')

	# add arguments
	parser.add_argument('--path', default = '/people/cs/s/sanda/cs6322/Cranfield', type = str)

	# execute main
	main(parser.parse_args())
