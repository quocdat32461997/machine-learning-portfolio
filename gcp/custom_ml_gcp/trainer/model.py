# import dependencies
import tensorflow as tf

def input_fn(path, height, widht, batch_size, seed = 2021):
	"""
	Load data, map transformations, and convert to tf.data API
	Args:
		path : path to images
		height : desired image height
		width : desired image width
		batch_size : number of samples per batch
		seed : random seed
	Returns:
		dataset : tf.data.Dataset instance
	"""

	# convert images to tf.data.Datast objects
	train_dataset = tf.keras.preprocessing.image_dataset_from_directory(path,
		validation_split = 0.2,
		subset = 'training',
		seed = seed,
		image_size = (height, width),
		batch_size = batch_size)

	val_dataset = tf.keras.preprocessing.image_dataset_from_directory(path,
		validation_split = 0.2,
		subset = 'validation',
		seed = seed,
		image_size = (height, width),
		batch_size = batch_size)

	#  map transformations
	train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size = tf.data.AUTOTUNE)
	val_dataset = val_dataset.cache().prefetch(buffer_size = tf.data.AUTOTUNE)

	# preprocessing (this step needs to handled separately when in prediction)
	normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
	train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
	val_datast = val_dataset.map(lambda x, y: (normalization_layer(x), y))

	return train_dataset, val_dataset
