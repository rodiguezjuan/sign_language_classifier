import tensorflow as tf
from tensorflow import keras

def load_model():
    model = keras.models.load_model('../data\model.hdf5')
    #print('Model Loaded!')
    #model.summary()

    return model