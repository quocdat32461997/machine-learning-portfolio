# import dependencies
from collections import defaultdict
from input import preprocess

class NaiveBayes(object):
    """
    Implementation of multinomial Naive Bayes
    """
    def __init__(self, preproc):
        self.preproc = preproc

        # probability
        self._ham_prob = defaultdict(int)
        self._spam_prob = defaultdict(int)

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
            text = preprocess(text)

        # tokenize
        tokens = text.split(' ')

        return tokens

    def train(self, input):
        """
        Train Naive Bayes model given input
        Args:
            input : Input object
        Returns: None
        """
        return None

    def predict(self, input):
        """
        Perform predictions
        Args:
            input : str
        Returns:
            output : TBD
        """

        # parse input
        input = self._parse(input)

        # compute probability

        # classify
        return 0

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
