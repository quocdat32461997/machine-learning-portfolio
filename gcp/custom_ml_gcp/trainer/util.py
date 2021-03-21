# import dependencies
import tensorflow as tf
import pathlib

def load_data():
	"""
	Load flowers data
	Args:
	Return:
		data_dir : path to data dir
	"""

	# define data url
	dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

	# download data into drive
	data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)

	# get list of files
	data_dir = pathlib.Path(data_dir)

	return data_dir
