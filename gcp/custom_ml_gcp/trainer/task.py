# import dependencies
import os
import argparse
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
	parser.add_argument(
		'--model-name', type = str,
		help = 'Name of your mode', default = 'cnn')
        parser.add_argument(
                '--job-dir', type = str,
                help = 'local or Google Cloud Storage location for writing checkpoints and exporting models',
                default = 'checkpoints')
        parser.add_argument('--num-epochs',
                type = int, default = 20,
                help = 'number of iterations to go through the data, default = 20')
        parser.add_argument('--batch-size',
                type = int, default = 128,
                help = 'number of samples to read for each training step, default = 128')
        parser.add_argument('--learning-rate',
                type = float, default = 0.1,
                help = 'learning rate for gradient descent, default = 0.1')
        parser.add_argument('--verbosity',
                choices = ['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
                default = 'INFO')
        parser.add_argument('--predict-num',
                type = int, default = 1, help = 'Number of predictions. If 1, online prediction. If > 1, batch prediction')

        return parser.parse_args()

def train_and_evaluate(args):
	
	# load data
	data_dir = util.load_data()
	train_dataset, val_dataset = model.input_fn(data_dir, height = 180, width = 180, batch_size = args.batch_size)

	# create model
	network = model.create_model()

	# create training dataset

	# create validation dataset

	# setup hyperparameters

	# train model

	# export model
	export_path = os.path.join(args.job_dir, args.model_name, str(floor(datetime.utcnow().timestamp())))
	tf.keras.models.save_model(network, export_path)
	return None
