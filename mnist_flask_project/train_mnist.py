# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:25:47 2019

@author: anshu
"""

from keras.datasets import mnist
from keras import models,layers
from keras.utils import to_categorical

class train_mnist:
    def __init__(self,epochs=10,batch_size=1000,validation_split=0.1):
        """
        The function accepts the parameters to train the deep learning model on
        mnist dataset
        attributes are - 
        epochs = number of epochs you wish to train the model
        batch_size = number of images to be used in one iteration
        validation_split = the data split from trainset for validation
        """
        self.batch_size = batch_size
        self.epochs = epochs
        self.validation_split = validation_split
        (self.xtrain,self.ytrain),(self.xtest,self.ytest)=mnist.load_data()
        self.xtrain = self.xtrain.reshape(60000,28,28,1)
        self.xtest = self.xtest.reshape(10000,28,28,1)
        self.xtrain = self.xtrain/255
        self.xtest = self.xtest/255
        self.ytrain = to_categorical(self.ytrain)
        self.ytest = to_categorical(self.ytest)
        self.train()
        
    def train(self):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(10,(3,3),input_shape=(28,28,1),activation='relu'))
        self.model.add(layers.MaxPooling2D(pool_size=(2,2)))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(10,activation='softmax'))
        self.model.compile(optimizer='adam',loss='categorical_crossentropy',
                           metrics=['accuracy'])
        self.model.fit(self.xtrain,self.ytrain,batch_size=self.batch_size,
                       epochs=self.epochs,verbose=True,
                       validation_split=self.validation_split)
        self.test_loss,self.test_acc = self.model.evaluate(self.xtest,self.ytest)
        print("Test Accuracy = ",self.test_acc)
        print("Test Loss = ",self.test_loss)
        self.model.save("models/mnist_model.h5")
        
if __name__=="__main__":
    train_mnist()
        
        
        
