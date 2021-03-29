# import dependencies
import os
import argparse
import numpy as np

from model import NaiveBayes, LogisticRegressor

np.random.seed(42)

def get_args():
    """
    Look for command-line arguments
    Args: None
    Returns:
        args : a dictionary of arugments
    """
    # initialize argument parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('--train-data', type = str, help = 'Path to training data', default = './train')
    parser.add_argument('--val-data', type = str, help = 'Path to validationo data', default = './test')

    # parse arguments
    args = parser.parse_args()

    return args
    
def main(args):
    """
    Execute text classification
    """
    lambdas = np.arange(0.0001, 0.0011, 0.0001)

    print('Without text-preprocessing')
    # train models: naive_bayes and logisitic_regressor
    naive_bayes = NaiveBayes(args.train_data, preproc = False)
    naive_bayes.train()
    print('Naive Bayes train-acc', naive_bayes.evaluate(args.train_data))
    print('Naive Bayes val-acc', naive_bayes.evaluate(args.val_data))

    for alpha in lambdas:
        logistic_regressor = LogisticRegressor(path = args.train_data, preproc = False,
            regularizer = 'l2', alpha = alpha, lr = 0.01, num_iter = 100)
        logistic_regressor.train()
        train_acc = logistic_regressor.evaluate(args.train_data)
        print('Logistic Regression train-acc given l2-regularizer at lambda {} = {}'.format(alpha, train_acc))
        val_acc = logistic_regressor.evaluate(args.val_data)
        print('Logistic Regression val-acc given l2-regularizer at lambda {} = {}'.format(alpha, val_acc))

    print('\nWith text-preprocessing')
    # train models: naive_bayes and logisitic_regressor
    naive_bayes = NaiveBayes(args.train_data, preproc = True)
    naive_bayes.train()
    print('Naive Bayes train-acc', naive_bayes.evaluate(args.train_data))
    print('Naive Bayes val-acc', naive_bayes.evaluate(args.val_data))

    for alpha in lambdas:
        logistic_regressor = LogisticRegressor(path = args.train_data, preproc = True,
            regularizer = 'l2', alpha = alpha, lr = 0.01, num_iter = 100)
        logistic_regressor.train()
        train_acc = logistic_regressor.evaluate(args.train_data)
        print('Logistic Regression train-acc given l2-regularizer at lambda {} = {}'.format(alpha, train_acc))
        val_acc = logistic_regressor.evaluate(args.val_data)
        print('Logistic Regression val-acc given l2-regularizer at lambda {} = {}'.format(alpha, val_acc))
if __name__ == '__main__':
    # get args
    args = get_args()

    # execute test classification
    main(args)
