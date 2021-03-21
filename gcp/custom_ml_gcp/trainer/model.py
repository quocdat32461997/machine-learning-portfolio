# import dependencies
import os
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

    # get list of files
    dataset = tf.data.Dataset.list_files(str(path/'*/*'))

    # convert images to tf.data.Datast objects
    @tf.function
    def parse_label(label):
        if label == 'sunflowers':
            return 0
        elif label == 'daisy':
            return 1
        elif label == 'roses':
            return 2
        elif label == 'tulips':
            return 3
        else:
            return 4
        
    @tf.function
    def parse_image(filename):
        parts = tf.strings.split(filename, os.sep)
        label = parts[-2]

        image = tf.io.read_file(filename)
        image = tf.image.decode_jpeg(image)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize_with_pad(image, height, width, method = tf.image.ResizeMethod.BILINEAR)
        image = tf.image.per_image_standardization(image)

        label = parse_label(label)
        return image, label
    dataset = dataset.map(parse_image)

    #  map transformations
    dataset = dataset.cache().shuffle(1000).batch(batch_size)

    return dataset.prefetch(buffer_size = tf.data.AUTOTUNE)

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
