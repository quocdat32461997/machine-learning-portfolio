"""
Author: Firstname Lastname
File: model.py
"""

# import dependencies
import tensorflow as tf

def input_fn(features, labels, shuffle, num_epochs, batch_size):
	"""
	input_fn - function to generate TF dataset
	Inputs:
		features : data features (labels excluded)
		labels : ground truth
		shuffle : boolean
		num_epochs : int
		batch_size : int
	Outputs:
		dataset : TF dataset instance
	"""

	if labels is None:
		inputs = features # evaluation
	else:
		inputs = (features, labels)

	# initialize TF dataset instance
	dataset = tf.data.Dataset.from_tensor_slices(inputs)

	# map transformations
	dataset = dataset.shuffle(buffer_size = len(features)) if shuffle else dataset # shuffle
	dataset = dataset.batch(batch_size)

	return dataset

def create_model(input_dim, learning_rate):
	"""
	create_model - function to create model
	Inputs:
		input_dim : tuple of integers
			feature dimension
		learning_rate : float
	Outputs:
		model : tf.keras.model instance
	"""
	# initialize model
	dense = tf.keras.layers.Dense
	model = tf.keras.Sequential([
		dense(100, activation = tf.keras.activations.relu, kernel_initializer = 'uniform',
			input_shape = (input_dim,)),
		dense(75, activation = tf.keras.activations.relu),
		dense(50, activation = tf.keras.activations.relu),
		dense(25, activation = tf.keras.activations.relu),
		dense(1, activation = tf.keras.activations.sigmoid)])

	# initialize optimizer
	optimizer = tf.keras.optimizers.Adam(lr = learning_rate)

	# compile model
	model.compile(loss = 'binary_crossentropy',
		optimizer = optimizer, metrics = ['accuracy'])

	return model
