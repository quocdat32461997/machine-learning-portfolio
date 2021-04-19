"""
Author: Dat Quoc Ngo
NET-ID: dqn170000
Date: April 19, 2021
File: main.py - execution in homework 2
"""

# import dependencies
import os
import re
import sys
import nltk
import argparse
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

import index
import utils

def main(args):
    """
    Implement Single-Pass In-Memory Indexing
    """

    # retrieve list of text files
    files = os.listdir(args.path)
    files = [os.path.join(args.path, x) for x in files]

    # get stop words
    with open('./stop_words.txt') as file:
        stop_words = file.read().split()

    # construct index
    print('Index Construction')

    # build index with lemmas
    lem_docs = index.Documents()
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        doc = index.Document(doc_idx = f_idx)
        doc.parse(text, stop_words, proc_fn = utils.lem)
        lem_docs.update(doc)

    ## merge into big index
    lem_index = index.Index()
    lem_index.build(lem_docs)
    lem_posting, lem_dict = lem_index.invert()

    # compressd dictionary
    lem_dict.compress(k = 4, method = 'blocking')

    # compress posting list
    lem_posting.compress(method = 'gamma')

    #**************************

    # build index with stems
    stem_docs = index.Documents()
    for file, f_idx in zip(files, range(1, len(files) + 1)):
        # read text
        with open(file) as f:
            text = f.read()

        # parse
        doc = index.Document(doc_idx = f_idx)
        doc.parse(text, stop_words, proc_fn = utils.stem)
        stem_docs.update(doc)

    ## merge to a big index
    stem_index = index.Index()
    stem_index.build(stem_docs)
    stem_posting, stem_dict = stem_index.invert()

    # compress dictionary
    stem_dict.compress(k = 4, method = 'front-coding')

    # compress posting
    stem_posting.compress(method = 'delta')

if __name__ == '__main__':
    # initialize argument parser
    parser = argparse.ArgumentParser(description = 'Argument parser for homework 1')

    # add arguments
    parser.add_argument('--path', default = './Cranfield', type = str)

    # execute main
    main(parser.parse_args())
