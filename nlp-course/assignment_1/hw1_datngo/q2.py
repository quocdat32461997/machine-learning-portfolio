"""
Author: Dat Quoc Ngo
Last modified: Feb. 13, 2021
"""

# import dependencies
import argparse
import re

def main(args):
	# read file
	with open(args.file, 'r') as file:
		text = file.read().split('\n')

	# regex matcher
	pattern = r'\b(([1-9]\d{2})|(\d[1-9]\d)|(\d{2}[1-9]))[-]{0,1}\d{2}[-]{0,1}(([1-9]\d{3})|(\d[1-9]\d{2})|(\d{2}[1-9]\d)|(\d{3}[1-9]))\b'

	# print matches
	for txt in text:
		# search ssn
		match = re.search(pattern, txt)

		# if a match, print out
		if match:
			print("Find {}".format(match.string))

if __name__ == '__main__':
	# initialize argument-parser object
	parser = argparse.ArgumentParser()

	# add arguments
	parser.add_argument('--file', help = 'Path to SSN file', default = 'ssn.txt')
	main(parser.parse_args())
