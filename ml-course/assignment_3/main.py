# import dependencies
import os
import argparse

from model import naive_bayes, logistic_regressor
from input import Input

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
    parser.add_argument('--method', type = str, choices = ['naive', 'logistic'], required = True)
    parser.add_argument('--num-epoch', type = int, default = 20)
    parser.add_argument('--train-data', type = str, help = 'Path to training data', default = './train')
    parser.add_argument('--val-data', type = str, help = 'Path to validationo data', default = './tset')

    # parse arguments
    args = parser.parse_known_args()

    return args
    
def main(args):
    """
    Execute text classification
    """

    # load data
    train_data = Input(path = './train')
    print(train_data._ham_vocabs, train_data._spam_vocabs)

    # preprocess data

    # train models: naive_bayes and logisitic_regressor

    # evaluate

    # print result

if __name__ == '__main__':
    # get args
    args = get_args()

    # execute test classification
    main(args)
