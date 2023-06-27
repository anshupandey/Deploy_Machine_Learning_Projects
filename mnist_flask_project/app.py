# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:31:26 2019

@author: anshu
"""

from flask import Flask,request,jsonify
import os
import cv2
from train_mnist import train_mnist
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
import numpy
import tensorflow as tf
#global graph
#graph = tf.get_default_graph()
app = Flask(__name__)


def load_model():
    if "mnist_model.h5" not in os.listdir('models'):
        train_mnist()
    model = models.load_model("models/mnist_model.h5")
    return model

model = load_model()

@app.route('/',methods=["GET","POST"])
def main():
    data = request.files.get('image','')
    data.save('img.jpg')
    img = image.img_to_array(image.load_img('img.jpg',target_size=(28,28),grayscale=True))
    #with graph.as_default():
    output = model.predict(img.reshape(1,28,28,1))
    output = numpy.argmax(output)
    return jsonify(str(output))

if __name__ == "__main__":
    app.run(debug=True)