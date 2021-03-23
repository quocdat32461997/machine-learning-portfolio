# import dependencies
import os
import spacy
import numpy as np

from collections import defaultdict

def preprocess(text):
    """
    Performs preprocessing s teps e.g. stopword removals
    Args:
        text : str
    Returns:
        text : str
            Preprocessed text
    """

    return text

class Input:
    def __init__(self, path, preproc = False):
        self.preproc = preproc
        self.path = path
        self._ham_vocabs = defaultdict(int)
        self._spam_vocabs = defaultdict(int)

        # build vocabs
        self._input_fn()

    def _parse(self, text, cls):
        """
        Parse text into tokens and update vocabs
        Arts:
            text : str
                Raw text
            cls : str
                Class/category of data
        """
        # preprocess
        if self.preproc:
            text = preprocess(text)
        
        # tokenize
        tokens = text.split(' ')

        # update vocabs
        if cls == 'spam':
            for token in tokens:
                self._spam_vocabs[token] += 1
        else:
            for token in tokens:
                self._ham_vocabs[token] += 1

    def _input_fn(self):
        """
        Process and transformed in preferred format
        Args: None
        Returns:
            data : np.array
        """

        # spam
        for cls in ['spam', 'ham']:
            class_path = os.path.join(self.path, cls)
            for file in os.listdir(class_path):
                # read text
                with open(os.path.join(class_path, file), encoding = 'utf-8', errors = 'ignore') as f:
                    text = f.read()

                # parse text
                self._parse(text, cls)

