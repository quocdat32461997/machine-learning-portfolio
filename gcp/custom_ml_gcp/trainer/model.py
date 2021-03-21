# import dependencies
import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense

def input_fn(path, height, width, batch_size, seed = 2021):
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
    train_dataset = train_dataset.cache().shuffle(1000)
    val_dataset = val_dataset.cache()

    # resize
    resize_method = lambda img, labels: (tf.image.resize_with_pad(img, height, width, method = tf.image.ResizeMethod.BILINEAR), labels)
    train_dataset = train_dataset.map(resize_method)
    val_dataset = val_dataset.map(resize_method)

    # preprocessing (this step needs to handled separately when in prediction)
    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
    train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
    val_datast = val_dataset.map(lambda x, y: (normalization_layer(x), y))

    return train_dataset.prefetch(buffer_size = tf.data.AUTOTUNE), val_dataset.prefetch(buffer_size = tf.data.AUTOTUNE)

def create_model(num_class, shape):
    """
    Initialize VGG16
    Args:
        num_class : number of classes
        shape : tuple of int
            (h, w, c)
    """
    inputs = tf.keras.Input(shape = shape)

    # retrieve pretrained VGG16
    vgg16 = tf.keras.applications.VGG16(
            include_top = False, weights = 'imagenet', input_shape = shape)


    # feed-forward
    outputs = vgg16(inputs)
    outputs = Flatten()(outputs)
    outputs = Dense(4096, activation = 'relu', activity_regularizer = 'l2')(outputs)
    outputs = Dense(4096, activation = 'relu', activity_regularizer = 'l2')(outputs)
    outputs = Dense(num_class, activation = 'softmax')(outputs)

    return tf.keras.Model(inputs = inputs, outputs = outputs)
