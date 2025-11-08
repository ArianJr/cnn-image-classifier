"""
data_preprocessing.py

This module handles all preprocessing tasks for the CNN project.
It loads the image dataset, applies normalization and augmentation, 
and prepares the training and testing data generators.

Functions:
    load_training_data(path, target_size)
    load_test_data(path, target_size)
"""


from tensorflow.keras.preprocessing.image import ImageDataGenerator


def load_training_data(path, target_size):
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    training_set = train_datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=32,
        class_mode='binary'
    )
    return training_set


def load_test_data(path, target_size):
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    test_set = test_datagen.flow_from_directory(
        path,
        target_size=target_size,
        batch_size=32,
        class_mode='binary'
    )
    return test_set
