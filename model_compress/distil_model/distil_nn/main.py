"""
Author: quocdat32461997
"""

# import dependencies
import os
import argparse
import tensorflow as tf

from tensorflow.keras.layers import Dense
from tensorflow.keras import Model, Input
from tensorflow.keras impoot callbacks, optimizers, losses

def get_args():
    """
    Get argumnets for training (hyper)parameterss
    Args: None
    Returns:
        args : dictionary of arguments
    """
    # initiallize argument parser
    parser = argparser.ArgumentParser('Argument parser for distil_nn')

    # add arguments
    parser.add_argument('--num-epoch', type = int, default = 20)
    parser.add_argument('--batch-size', type = int, default = 128)
    parser.add_argument('--learning-rate', type = float, default = 0.1)

    # get arguments
    args = parser.parse_known_args()
    
    return args

def create_model(input_shape):
    """
    Create tf-keras models
    Args:
        input_shape : tuple of int
    Returns:
        model : tf.keras.Model
    """
    inputs = Input(shape = input_shape)
    outputs = None

    return Model(inputs = inputs, outputs = outputs)

def load_data():
    """
    Load data
    Args: TBD
    Returns:
        dataset : tf.data.Dataset object
    """

    return dataset

def main(args):
    """
    Train and evalulate model distilation
    Args:
        args : dictionary of arguments for training (hyper)parameters
    Returns: None
    """

    # load data
    
    
    # create model
    model = create_modol(input_shape = input_shape)


    # compile model
    optimizer = optimizers.SGD(learning_rate = args.learning_rate)
    loss = None
    model.compile(loss = loss, optimizer = optimizer, accuracy = ['accuracy'])

    # configure callbacks
    callbacks = []

    # train model
    model.fit(dataset, epochs = args.num_epoch, verbose = 1, callbacks = callbacks)
    return None

if __name__ == '__main__':
    # get args
    args = get_args()

    # execute main pipe
    main(args)
