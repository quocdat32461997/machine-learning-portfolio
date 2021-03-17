"""
Author: Firstname Lastname
File: task.py
"""

#import dependencies
import os
import argparse
import tensorflow as tf

from . import model
from . import util

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
	"""
	train_and_evaluate - function to train & evaluate TF models
	Inputs:
		args : dictionary of arguments
	Outputs: _
	"""

	# load data
	train_x, train_y, eval_x, eval_y = util.load_data()

	num_train_examples, input_dim = train_x.shape # retrieve number of training samples

	# create model
	network = model.create_model(input_dim = input_dim,
		learning_rate = args.learning_rate)

	# create training dataset
	training_dataset = model.input_fn(
		features = train_x.values,
		labels = train_y,
		shuffle = True,
		num_epochs = args.num_epochs,
		batch_size = args.batch_size)

	# create validation dataset
	validation_dataset = model.input_fn(
		features = eval_x.values,
		labels = eval_y,
		shuffle = False,
		num_epochs = args.num_epochs,
		batch_size = args.predict_num)

	# setup hyperparameters
	lr_scheduler = tf.keras.callbacks.LearningRateScheduler(
		lambda epoch: args.learning_rate + 0.02 * (0.5 **(1 + epoch)),
		verbose = True)
	tensorboard = tf.keras.callbacks.TensorBoard(
		os.path.join(args.job_dir, 'tensorboard'),
		histogram_freq = 1)

	# train model
	network.fit(
		training_dataset,
		steps_per_epoch = int(num_train_examples / args.batch_size), #mini-batch-size
		epochs = args.num_epochs,
		validation_data = validation_dataset,
		validation_steps = 1, # validation_step = 1 in prediction if training is mini-batching
		verbose = 1,
		callbacks = [lr_scheduler, tensorboard])

	# export model
	export_path = os.path.join(args.job_dir, 'trained_model')
	tf.keras.models.save_model(network, export_path)

	return None

if __name__ == '__main__':
	args = get_args()
	tf.compat.v1.logging.set_verbosity(args.verbosity)
	train_and_evaluate(args)
