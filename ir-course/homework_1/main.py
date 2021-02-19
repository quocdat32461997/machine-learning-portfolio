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

def tokenize(text):
	"""
	tokenize - function to perform tokenization
	Inputs:
		- 
		-
	Outputs:
		- 
	"""
	# strip heading, tailing, and in-middle whitepsace
	text = re.sub(pattern = '[ ]+', repl = ' ', string = text)

	# substitue puncutations with whitespace
	text = re.sub(pattern = '[.!?\\-<>]*', repl = '', string = text)

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

	for file in files:
		# read text
		with open(file) as f:
			text = f.read()
		# process
		text = process(text)
		print(text)
		print()
		# tokenization
		tokens = tokenize(text)
		print(tokens)
		input()
		# stemming

	return None

if __name__ == '__main__':
	# initialize argument parser
	parser = argparse.ArgumentParser(description = 'Argument parser for homework 1')

	# add arguments
	parser.add_argument('--path', default = '/people/cs/s/sanda/cs6322/Cranfield', type = str)

	# execute main
	main(parser.parse_args())
