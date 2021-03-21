# import dependencies
import os
import argparse
import numpy as np
import tensorflow as tf
from datetime import datetime

from . import util
from . import model

def get_args():
    """
    Arugment parser
    Inputs: _
    Outputs:
        args : dictionary of arguments
    """
    # initialize argument parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('--model-name', type = str,
        help = 'Name of your mode', default = 'cnn')
    parser.add_argument('--job-dir', type = str,
        help = 'local or Google Cloud Storage location for writing checkpoints and exporting models',
        default = 'checkpoints')
    parser.add_argument('--num-epochs',
        type = int, default = 20,
        help = 'number of iterations to go through the data, default = 20')
    parser.add_argument('--batch-size',
        type = int, default = 32,
        help = 'number of samples to read for each training step, default = 128')
    parser.add_argument('--learning-rate',
        type = float, default = 0.001,
        help = 'learning rate for gradient descent, default = 0.1')
    parser.add_argument('--verbosity',
        choices = ['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
        default = 'INFO')
    parser.add_argument('--predict-num',
        type = int, default = 1, help = 'Number of predictions. If 1, online prediction. If > 1, batch prediction')

    return parser.parse_args()

def train_and_evaluate(args):
    # height and width
    height, width = 224, 224

    # load data
    data_dir = util.load_data()

    # create train and validation datasets
    train_dataset = model.input_fn(data_dir, height = height, width = width, batch_size = args.batch_size)
    for x in train_dataset.take(1):
        print(x[0].shape, x[1])

    # create model
    network = model.create_model(num_class = 5, shape = (height, width, 3))
    print(network.summary())

    # setup hyperparameters
    loss = tf.keras.losses.SparseCategoricalCrossentropy()
    optimizer = tf.keras.optimizers.Adam(learning_rate = args.learning_rate)
    callbacks = []

    network.compile(loss = loss, optimizer = optimizer, metrics = ['accuracy'])

    # train model
    network.fit(train_dataset, epochs = args.num_epochs, batch_size = args.batch_size, verbose = 1, callbacks = callbacks)
    # export model
    export_path = os.path.join(args.job_dir, args.model_name, str(np.floor(datetime.utcnow().timestamp())))
    tf.keras.models.save_model(network, export_path)
    return None

if __name__ == '__main__':
    args = get_args()
    train_and_evaluate(args)
