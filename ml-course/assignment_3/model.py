# import dependencies
import os
import numpy as np
from collections import defaultdict

class NaiveBayes(object):
    """
    Implementation of multinomial Naive Bayes
    """
    def __init__(self, path, classes = ['spam', 'ham'], preproc = True):
        self.classes = classes
        self.preproc = preproc
        self.path = path

        self.class_term = {}
        self.class_priors = {}
        self.class_prob = {}
        self.vocab_size = []

    def _preprocess(self, text):
        """
        Preprocesses text
        Args:
            text : str
        Returns:
            text : str
                Preprocessed text
        """
        return text

    def _parse(self, text):
        """
        Parse text into tokens
        Args:
            text : str
        Returns:
            tokens : list
                List of tokens
        """

        # preprocess
        if self.preproc:
            text = self._preprocess(text)

        # tokenize
        tokens = text.split(' ')

        return tokens

    def _count(self, tokens):
        """
        Counts frequency of terms
        Args:
            tokens : list of str
        Returns:
            output ; dict
                frequency of dictionary
        """
        output = defaultdict(int)

        for token in tokens:
            output[token] += 1

        return output

    def _condprob(self, input):
        """
        Computes conditional probability for each term
        Args:
            input : defaultdict(int)
                Frequency dictionary of terms
        Returns:
            output : defaultdict(float)
                Dictionary of term's conditional probability
        """
        output = defaultdict(float)
        normalize_term =  self.vocab_size + sum(list(input.values()))

        for vocab, freq in input.items():
            output[vocab] = (freq + 1) / normalize_term

        return output

    def train(self):
        """
        Train Naive Bayes model given input
        Args: None
        Returns: None
        """

        # for each class
        class_doc = {}
        for cls in self.classes:
            path = os.path.join(self.path, cls)
            files = os.listdir(path)

            # count docs in a class
            class_doc[cls] = len(files)

            # concatenate all class text
            text = ' '.join([open(os.path.join(path, file), encoding = 'utf-8', errors = 'ignore').read() for file in files])

            # parse text
            tokens = self._parse(text)

            # count tokens of term
            self.class_term[cls] = self._count(tokens)

            # add vocabs
            self.vocab_size += list(self.class_term[cls].keys())

        # compute total docs and class-priors
        doc_num = sum(list(class_doc.values()))
        for cls in self.classes:
            self.class_priors[cls] = np.log(class_doc[cls] / doc_num)

        # compute vocab size
        self.vocab_size = len(set(self.vocab_size))

    def _compute_prob(self, tokens):
        """
        Compute the Naive Bayes probability given list of tokens
        Args:
            tokens : list of str

        Returns:
            output : float
        """
        output = []
        for cls in self.classes:
            # compute normalize term
            normalize_term = self.vocab_size + sum(list(self.class_term[cls].values()))

            # compute conditional prob
            output.append(self.class_priors[cls] + sum([
                np.log((self.class_term[cls][token] + 1) / normalize_term) for token in tokens]))

        return self.classes[np.argmax(output)]

    def predict(self, input):
        """
        Perform predictions
        Args:
            input : str
        Returns:
            output : conditional prob
        """

        # parse input
        tokens = self._parse(input)

        # compute probability
        output = self._compute_prob(tokens)

        # classify
        return output

class LogisticRegressor(object):
    """
    Implementation of Logistic Regression
    """
    def __init__(self):
        pass

    def predict(self, input):
        """
        Perform predictions
        Args:
            input : str
        Returns:
            output : TBD
        """

        return 0
