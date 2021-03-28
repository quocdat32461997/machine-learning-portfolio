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

    print('POS for the folowing text {}'.format(input))

    # process text
    assert len(input) > 0, 'Length of test input msut be greater than 0'
    input = _process_test(input)

    probs, tags = _compute_bigram_prob(input)

    # compute the final output
    output = reduce(lambda x, y: x*y, probs)
    if output == 0:
        print("Suggested post-tags (excluding out-of-vocab) are {}".format(" ".join(tags)))
        print("The final probabillity for the POS-Tag sequene is {}. Hence, the post-tags for the input text could not be determined".format(output))
    else:
        print("The final probability for the POS-Tag sequene is {}".format(output))
        for word, tag in zip(input, tags[1:-1]):
            print("Word {} - Tag {}".format(word, tag))

    return None

def main(args):
    # read data corpus
    with open('NLP6320_POSTaggedTrainingSet-Unix.txt') as file:
        data = file.read()
	
    # process text
    data = process(data)

    # compute unigram & bigram model
    bigram_tag, unigram_tag, word_tag, bigram_tag_prob, word_tag_prob = build_bigram(data)

    # test
    test = 'Brainpower has the power .'
    bigram_prob = predict(test, unigram_tag, bigram_tag, word_tag, bigram_tag_prob, word_tag_prob)

    return None

if __name__ == '__main__':
    # initialize parser
    parser = argparse.ArgumentParser()

    # execute
    main(parser.parse_args())
