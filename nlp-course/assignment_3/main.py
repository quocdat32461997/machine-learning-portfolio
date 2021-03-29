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
        - words : list
	    List of words
        - tags : list
            List of pos tags
    """
    # split by whitespace
    input = re.split(pattern = '[\s]+', string = input)

    # find words in WORD_POS pattern
    valid_word = lambda x: True if re.findall(pattern = r'[a-zA-Z]*_[a-zA-Z]*', string = x) else False
    words = []
    tags = []
    for token in input:
    	if valid_word(token):
            word, pos = token.split('_')
            words.append(word)
            tags.append(pos)

    return words, tags

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
        bigram_tag : dict
        unigram_tag : dict
        word_tag : dict
        bigram_tag_prob : dict
        word_tag_prob : dict
    """
	
    # initialize unigram & bigram
    bigram_tag, unigram_tag = defaultdict(int), defaultdict(int)
    word_tag = defaultdict()

    # iterate thru tokens
    for words, tags in input:
        if words:
            unigram_tag['<s>'] += 1
            unigram_tag['</s>'] += 1
            unigram_tag[tags[0]] += 1
            word_tag[words[0]] = defaultdict(int) if not words[0] in word_tag else word_tag[words[0]]
            word_tag[words[0]][tags[0]] += 1

            bigram_tag[tuple(['<s>', tags[0]])] += 1 # bigram <s> tag_0
            for idx in range(1, len(words)):
                unigram_tag[tags[idx]] += 1
                bigram_tag[tuple(tags[idx - 1 : idx + 1])] += 1
                
                if not words[idx] in word_tag:
                    word_tag[words[idx]] = defaultdict(int)
                else:
                    word_tag[words[idx]][tags[idx]] += 1
            bigram_tag[tuple([tags[-1],'</s>'])] += 1 # bigram: last_tag </s>

    # compute bigram prob and bigram-frequency
    bigram_tag_prob, word_tag_prob = defaultdict(float), defaultdict()
    for word, tag_count in word_tag.items():
        word_tag_prob[word] = defaultdict(float)
        for tag, count in tag_count.items():
            word_tag_prob[word][tag] = count / unigram_tag[tag]

    for bigram, count in bigram_tag.items():
        bigram_tag_prob[bigram] = count / unigram_tag[bigram[0]]

    return bigram_tag, unigram_tag, word_tag, bigram_tag_prob, word_tag_prob

def predict(input, unigram_tag, bigram_tag, word_tag, bigram_tag_prob, word_tag_prob):
    """
    predict - function to compute bigram probability of the input sentence
    Inputs:
        input : str
            Sentence
    	unigram_tag : defaultdict
        bigram_tag : defaultdict
    	bigram_tag_prob : defaultdict
        word_tag_prob : defaultdict
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
        return re.split(pattern = '\s+', string = input)

    def _compute_bigram_prob(input, pointer = 0, probs = [1], tag_seq = ['<s>']):
        """
        _compute_bigram_prob
        Inputs:
            input : list 
                List of tokens
            pointer ; int
                Word inde, by default = 0x
            tag_seq : list
                Tag sequence, by default [ '<s>']
            probs : list of float
                Prob list for tags
        Outputs:
            output : float
                Bigram probability
	"""

        # base cacse
        if pointer == len(input):
            probs.append(bigram_tag[tuple([tag_seq[-1], '</s>'])] / unigram_tag[tag_seq[-1]])
            tag_seq.append('</s>')
            return probs, tag_seq
            # retrieve all tags of the current word
        elif not input[pointer] in word_tag:
            temp_probs, temp_tag_seq = _compute_bigram_prob(input, pointer + 1, probs + [0], tag_seq)
            return temp_probs, temp_tag_seq
        else:
            tags = word_tag[input[pointer]]
            best_seq = []
            best_probs = []
            for tag, count in tags.items():

                # compute state and transitiono prob
                tag_prob = bigram_tag[tuple([tag_seq[-1], tag])] / unigram_tag[tag_seq[-1]]
                word_prob = count / unigram_tag[tag]
                prob = tag_prob * word_prob

                # recursve to next woord
                temp_probs, temp_tag_seq = _compute_bigram_prob(input, pointer+1, probs + [prob], tag_seq + [tag])
                best_seq.append(temp_tag_seq)
                best_probs.append(temp_probs if isinstance(temp_probs, list) else [temp_probs])
            probs = [reduce(lambda x,y:x*y, probs) for probs in best_probs]

            idx = np.argmax(probs)
            return best_probs[idx], best_seq[idx]

    print('POS for the folowing text "{}"'.format(input))

    # process text
    assert len(input) > 0, 'Length of test input msut be greater than 0'
    input = _process_test(input)

    probs, tags = _compute_bigram_prob(input)

    # compute the final output
    output = reduce(lambda x, y: x*y, probs)
    if output == 0:
        print("Suggested post-tags (excluding out-of-vocab) are {}".format(" ".join(tags)))
        print("The final probabillity for the POS-Tag sequene is {}. Hence, the post-tags for the input text could not be determined\n".format(output))
    else:
        print("The final probability for the POS-Tag sequene is {}".format(output))
        for word, tag in zip(input, tags[1:-1]):
            print("Word {} - Tag {}".format(word, tag))
        print()

    return None

def part_1(args):
    # read data corpus
    with open('NLP6320_POSTaggedTrainingSet-Unix.txt') as file:
        data = file.read()
	
    # process text
    data = process(data)

    # compute unigram & bigram model
    bigram_tag, unigram_tag, word_tag, bigram_tag_prob, word_tag_prob = build_bigram(data)

    # test
    tests = ['Brainpower has the power .',
            'Janet will back the bill .',
            'I lost power yesterday .']
    for test in tests:
        bigram_prob = predict(test, unigram_tag, bigram_tag, word_tag, bigram_tag_prob, word_tag_prob)

    return None

def viberti(input, trans_matrix, observ_matrix, trans_rows, trans_cols, observ_rows, observ_cols):
    """
    viberti - applied Viberti algo to perform POS Tagging
    Args:
        input - list of str
        trans_matrix - np.array
        observ_matrix - np.array
        trans_rows : dict
        trans_cols : dict
        observ_rows : dict
        observ_cols : dict
    Returns:
        tags : list of tags
        probs : list of probs in regrads with tags
    """
    def _prob(word, prev_word_idx, tag, prev_tag):
        """
        Compute the probability = max(trans, observ)
        Args:
            word : current word
            prev_word_idx : previous word idx
            tag : current tag
            prev_tag : previous tag
        Returns:
            output : float
        """

        a = matrix[observ_rows[prev_tag], prev_word_idx] # observ_cols[prev_word]]
        b = trans_matrix[trans_rows[prev_tag], trans_cols[tag]]
        c = observ_matrix[observ_rows[tag], observ_cols[word]]
        return a * b * c

    # initiailze dynamic matrix
    matrix = np.zeros((len(observ_rows),len(input)))
    tag_matrix = np.zeros((len(observ_rows), len(input)), dtype = np.int32)

    # fill the first column
    for tag, t_idx in observ_rows.items():
        word = input[0]
        matrix[t_idx, 0] = trans_matrix[trans_rows['<s>'], trans_cols[tag]] * observ_matrix[t_idx, observ_cols[word]]

    # fill matrix
    for word, w_idx in zip(input[1:], range(1, len(input))):
        prev_word = input[w_idx - 1]
        for tag, t_idx in observ_rows.items():

            # compute prob in regards with previous state
            probs = [_prob(word, w_idx - 1, tag, prev_tag) for prev_tag in observ_rows.keys()]

            # fill slot
            idx = np.argmax(probs) # get the best previous-tag index
            matrix[t_idx, w_idx] = probs[idx]

            # fill tag matrix
            tag_matrix[t_idx, w_idx] = idx


    # trace back to retrieve best tags
    idx = np.argmax(matrix[:, -1]) # last tag
    probs = []
    tags = []
    for i in range(len(input) - 1, 0, -1):
        tags.append(list(observ_rows.keys())[idx]) # add tag
        probs.append(matrix[idx, i])
        idx = tag_matrix[idx, i] # next tag
    tags.append(list(observ_rows.keys())[idx]) # firs tag
    probs.append(matrix[idx, 0])
    tags = tags[::-1] # reverse tags
    probs = probs[::-1] # reverse probs following tags

    return tags, probs
def part_2():
    trans_matrix = np.array([
        [0.2767, 0.0006, 0.0031, 0.0453, 0.0449, 0.0510 ,0.2026],
        [0.3777, 0.110, 0.0009, 0.0084, 0.0584, 0.0090, 0.0025],
        [0.0008, 0.0002, 0.7968, 0.0005, 0.0008, 0.1698, 0.0041],
        [0.0322, 0.0005, 0.0050, 0.0837, 0.0615, 0.0514, 0.2231],
        [0.0366, 0.0004, 0.0001, 0.0733, 0.4509, 0.0036, 0.0036],
        [0.0096, 0.0176, 0.0014, 0.0086, 0.1216, 0.0177, 0.0068],
        [0.0068, 0.0102, 0.1011, 0.1012, 0.0120, 0.0728, 0.0479],
        [0.1147, 0.0021, 0.0002, 0.2157, 0.4744, 0.0102, 0.0017]])
    trans_rows = {'<s>': 0, 'NNP': 1, 'MD': 2, 'VB': 3, 'JJ': 4, 'NN': 5, 'RB': 6, 'DT': 7}
    trans_cols = {'NNP' : 0, 'MD': 1, 'VB': 2, 'JJ': 3, 'NN': 4, 'RB': 5, 'DT': 6}
    observ_matrix = np.array([
        [0.000032, 0, 0, 0.000048, 0],
        [0, 0.308431, 0, 0, 0],
        [0, 0.000028, 0.000672, 0, 0.000028],
        [0, 0, 0.000340, 0, 0],
        [0, 0.000200, 0.000223, 0, 0.002337],
        [0, 0, 0.010446, 0, 0],
        [0, 0, 0, 0.506099, 0]])
    observ_rows = {'NNP': 0, 'MD': 1, 'VB': 2, 'JJ': 3, 'NN': 4, 'RB': 5, 'DT': 6}
    observ_cols = {'Janet': 0, 'will': 1, 'back': 2, 'the': 3, 'bill': 4}
    
    tests = ['Janet will back the bill',
            'will Janet back the bill',
            'back the bill Janet will']
    
    # proccess text
    tests = [test.split(' ') for test in tests]

    # assign POS Tags
    pos_tags = []
    pos_probs = []
    for test in tests:
        tags, probs = viberti(test, trans_matrix, observ_matrix,
                trans_rows, trans_cols, observ_rows, observ_cols)
        pos_tags.append(tags)
        pos_probs.append(probs)
    
    # display results
    for test, tags, probs in zip(tests, pos_tags, pos_probs):
        print('POS Tags for "{}"'.format(' '.join(test)))
        for x, tag, prob in zip(test, tags, probs):
            print('Word {} - Tag {} - Prob {}'.format(x, tag, prob))

        print()

    return None

if __name__ == '__main__':
    # initialize parser
    parser = argparse.ArgumentParser()

    # execute
    print('POS Tagging with HMM')
    part_1(parser.parse_args())

    print("POS Tagging with HMM in Viberti coding algorithm")
    part_2()
