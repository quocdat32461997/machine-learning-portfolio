# import dependencies
import os
import re
import numpy as np
from collections import defaultdict

class ML(object):
    def __init__(self, preproc):
        self.preproc = preproc

    def _preprocess(self, text) :
        """
        Preprocess text
        Args:
            text : str
        Returns:
            text : str
                Preprocessed text
        """
        return re.sub(pattern = self.pattern, repl = '', string = text)

    def _parse(self, text):
        """
        Parase text into tokens
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


class NaiveBayes(ML):
    """
    Implementation of multinomial Naive Bayes
    """
    def __init__(self, path, classes = ['spam', 'ham'], preproc = True):
        self.classes = classes
        self.preproc = preproc
        self.path = path
        self.stopwords = '|'.join(open('./stopwords.txt').read().split())
        self.class_term = {}
        self.class_priors = {}
        self.vocab_size = []
        self.stopwords = open('./stopwords.txt').read().split()
        self.pattern = '|'.join(self.stopwords)

    def _count(self, tokens):
        """
        Counts frequency of terms
        Args:
            tokens : list of str
        Returns:
            output ; dict
                Dicitonary of word frequency
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

    def evaluate(self, path):
        """
        Evaluate Naive Bayes
        Args:
            path : path to test data
        Returns:
            acc : accuracy
        """

        # read test data
        input = {}
        for cls in self.classes:
            class_path = os.path.join(path, cls)
            input[cls] = [open(os.path.join(class_path, file), encoding = 'utf-8', errors = 'ignore').read()
                for file in os.listdir(class_path)]

        # make predictions
        output = {}
        for cls in self.classes:
            output[cls] = [self.predict(text) for text in input[cls]]

        # compute accuracy
        acc = []
        for cls, preds in output.items():
            acc.extend([cls == pred for pred in preds])

        acc = sum(acc) / len(acc)

        return acc

class LogisticRegressor(ML):
    """
    Implementation of Logistic Regression
    Assumes that the feature size is 100 (or top 100 features) based on the word frequency with add-one-smoothing
    """
    def __init__(self, path, lr = 0.1, regularizer = None, alpha = None, num_iter = 20, classes = ['spam', 'ham'], preproc = True):
        self.path = path
        self.num_iter = num_iter
        self.classes = classes
        self.preproc = preproc
        self.vocabs = defaultdict(int)
        self.vocab_size = None
        self.features = []
        self.weight_0 = None
        self.weights = None
        self.labels = []
        self.lr = lr
        assert not ((not regularizer) ^ (not alpha)),'Regularizer and alpha must be specified together' 
        self.regularizer = regularizer
        self.alpha = alpha
        self.stopwords = open('./stopwords.txt').read().split()
        self.pattern = '|'.join(self.stopwords)
    
    def _build_features(self):
        """
        Build word-frequency and vocabs for Logistic Regression
        """

        # build feature representation based on word frequency
        tokens = []
        for cls, idx in zip(self.classes, range(len(self.classes))):
            path = os.path.join(self.path, cls)
            files = os.listdir(path)
            self.labels.extend([idx]*len(files))

            # read text
            tokens.extend([self._parse(open(os.path.join(path, file), encoding = 'utf-8', errors = 'ignore').read()) for file in files])

        # store text
        self.features = tokens.copy()

        # collect text, tokens and count word per clss
        tokens = [w for sent in tokens for w in sent]

        # build vocabs
        vocabs = sorted(set(tokens))
        for x, y in zip(vocabs, range(len(vocabs))):
            self.vocabs[x] = y
        self.vocab_size = len(self.vocabs)

        # save text
        self.features = np.array([self._text2vector(sent) for sent in self.features], dtype = np.float128)

        # initialize weights
        self.weights = np.random.uniform(size = self.vocab_size)
        self.weight_0 = np.random.uniform(size = 1)

        self.labels = np.array(self.labels)

        del vocabs
        del tokens

    def _gradient_descent(self, features):
        """
        Computes gradient descents given loss
        Args:
            features : np.array
        Returns: None
        """
        loss = self.labels - features
        penalty = (self.alpha * self.lr * self.weights) if self.regularizer else 0
        self.weights += self.lr * np.dot(loss, self.features) - penalty

        #penalty_0 = (self.alpha * self.lr * self.weight_0) if self.regularizer else 0
        #self.weight_0 += self.lr * np.sum(loss) - penalty_0

    def _loss(self, preds, labels):
        """
        Compute entropy loss
        Args:
            preds : np.array
            lables : np.array
        Returns:
            loss : np.array of size vocab_size
        """
        epsilon = 1e-5
        predict_1 = labels * np.log(preds + epsilon)
        predict_0 = (1 - labels) * np.log(1 - preds + epsilon)

        return -sum(predict_1 + predict_0) / len(preds)

    def train(self):
        """
        Train MCAP Logistic Algorithm givne input
        Args: None
        Returns: None
        """

        # build feaetures
        self._build_features()

        # training
        for iter in range(self.num_iter):
            # make predictions
            preds = self._sigmoid(self.features)

            # compute loss
            loss = self._loss(preds, self.labels)

            # update weiights
            self._gradient_descent(preds)

            # acc
            #preds = np.array(preds)
            #preds = np.floor(preds + 0.5)
            #print('Iter: {} Loss: {} Acc: {}'.format(iter, loss, sum(preds == self.labels) / len(self.labels)))

    def _text2vector(self, input):
        """
        Convert text to feature vector
        Args:
            input : list of str
                List of tokens
        Returns:
            vector : list
                Feacture vector
        """

        # initialize feature vector
        vector = np.zeros(self.vocab_size) # avoid zero-divide

        # fill vector
        for token in input:
            if token in self.vocabs:
                vector[self.vocabs[token]] += 1

        return vector

    def _sigmoid(self, input):
        """
        Computes sigmoid outputsw
        Args:
            input : np.array
        Returns:
            output : np.array
        """
        val = np.dot(input, self.weights)
        val = np.clip(val, -500, 500)
        exp = np.exp(-val)
        return 1.0 / (1.0 + exp)

    def predict(self, input):
        """
        Perform predictions
        Args:
            input : str
        Returns:
            output : 1 or 0
        """

        # parse text
        input = self._parse(input)
        input = self._text2vector(input)

        # make predictions
        preds = self._sigmoid(input)
        preds = np.floor(preds + 0.5)
        return preds

    def evaluate(self, path):
        """
        Evaluate Naive Bayes
        Args:
            path : path to test data
        Returns:
            acc : accuracy
        """

        # read test data
        input = {}
        for cls, idx in zip(self.classes, range(len(self.classes))):
            class_path = os.path.join(path, cls)
            input[idx] = [open(os.path.join(class_path, file), encoding = 'utf-8', errors = 'ignore').read()
                for file in os.listdir(class_path)]

        # make predictions
        output = {}
        for cls, texts in input.items():
            output[cls] = [self.predict(text) for text in texts]

        # compute accuracy
        acc = []
        for cls, preds in output.items():
            acc.extend([cls == pred for pred in preds])

        acc = sum(acc) / len(acc)

        return acc
