"""
Author: quocdat32461997
"""

# import dependencies
import os
import argparse
import tensorflow as tf

from tensorflow.keras.layers import Dropout, Dense
from tensorflow.keras import Model, Input
from tensorflow.keras import callbacks, optimizers, losses

# set random seed
tf.random.set_seed(42)

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

def create_model(input_shape, unit_num, num_class, drop_rate = None, regularizer = None):
    """
    Create tf-keras models
    Args:
        input_shape : tuple of int
        unit_num : int
            Number of units per hidden layer
        num_class : int
            Number of classes or classificaiton output
        drop_rate : float
            Ratio of neurons to be dropped
        regularizer : str
            Name of regularizers applied on kernel weights
    Returns:
        model : tf.keras.Model
    """

    # input layer
    outputs = Input(shape = input_shape)

    # layer 1
    outputs = Dense(unit_num, activation = 'relu', kernel_regularizer = regularizer)(outputs)
    outputs = Dropout(rate = drop_rate)(outputs)

    # layer 2
    outputs = Dense(unit_num, activation = 'relu', kernel_regularizer = regularizer)(outputs)
    outputs = Dense(rate = drop_rate)(outputs)

    # classification layer
    outputs = Dense(num_class, activation = 'softmax')(outputs)

    return Model(inputs = inputs, outputs = outputs)

def load_data():
    """
    Load data
    Args: None
    Returns:
        dataset : tf.data.Dataset object
    """

    # load mnist data
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # convert to tf.data.Dataset objects
    to_dataset = tf.data.Dataset.from_tensor_slices
    x_train = to_dataset(x_train)
    y_train = to_dataset(y_train)
    x_test = to_dataset(x_test)
    y_test = to_dataset(y_test)

    # image processing
    def _img_proc(img):
        """
        Processes images
        Args:
            img : tensor
                Image tensor of shape [h, w, c] or [h, w]
        Returns:
            img : tensor
                Image tensor of shape [h, w, c] or [h, w]
        """

        # jitter up to 2 pixels
        img_shape = tf.shape(img)
        x, y = tf.random.uniform(shape = [], maxval = img_shape[0], dtype = tf.int32), tf.random.uniform(shape = [], maxval = img_shape[1], dtype = tf.int32)
        img[x][y] = 255

        x, y = tf.random.uniform(shape = [], maxval = img_shape[0], dtype = tf.int32), tf.random.uniform(shape = [], maxval = img_shape[1], dtype = tf.int32)
        img[x][y] = 255

        return img
    x_train = x_train.map(lambda img: _img_proc(img))
    x_test = x_test.map(lambda img: _img_proc(img))

    # zip to train & test datasets
    train_dataset = tf.data.Dataset.zip((x_train, y_train))
    test_dataset = tf.data.Dataset.zip((x_test, y_test))

    return train_dataset, test_dataset

def main(args):
    """
    Train and evalulate model distilation
    Args:
        args : dictionary of arguments for training (hyper)parameters
    Returns: None
    """

    # load data
    dataset = load_data()
    
    # create model
    drop_rate = 0.2
    regularizer = 'l2'
    teacher = create_modol(input_shape = input_shape, unit_num = 1200, num_class = num_class,
                drop_rate = drop_rate, regularizer = regularizer)
    student = create_model(input_shpae = input_shape, unit_num = 800, num_class = num_class)

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
