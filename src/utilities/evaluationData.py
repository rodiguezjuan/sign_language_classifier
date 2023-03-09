import numpy as np

import tensorflow as tf
from tensorflow.keras.models import load_model

url = "../data\data_array.npy"

def evaluation_data(model):
    data_video = np.load(url)
    data_video = np.expand_dims(data_video, axis = 0)
    print(data_video.shape)

    predict = model.predict(data_video)
    print(predict)

    index = tf.math.argmax(predict[0])
    index = tf.keras.backend.eval(index)
    print(index)
    return index
    
