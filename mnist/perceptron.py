import numpy as np
import mnist
import pdb
from descriptors import *

class perceptron_mnist:

    def __init__(self, learning_rate):
        self.trX, self.trY, self.teX, self.teY = mnist.load_data(
                one_hot=False, flatten=False)
        self.NCLASSES = 10
        self.w = None
        self.learning_rate = learning_rate

    def classify(self, features):
        scores = np.dot(features, self.w)
        guess = np.argmax(scores)
        return guess


    def train(self, get_features, nepochs):
        self.nfeatures = len(get_features(self.trX[0]))
        self.w = np.zeros((self.nfeatures, self.NCLASSES))
        nsamples = self.trX.shape[0]
        for epoch in range(nepochs):
            nerrors = 0 
            print('training epoch ' + str(epoch))
            for i in range(nsamples):
                image_class = self.trY[i]
                features = get_features(self.trX[i])
                predicted_class = self.classify(features)
                if predicted_class != image_class:
                    self.w[:, image_class] += self.learning_rate * features
                    self.w[:, predicted_class] -= self.learning_rate * features
                    nerrors += 1
            print('training errors: ' + str(nerrors))
        

    def test(self, get_features):
        ncorrect = 0
        for i in range(self.teX.shape[0]):
            features = get_features(self.teX[i])
            prediction = self.classify(features)
            if (prediction == self.teY[i]):
                ncorrect += 1
        print('success rate on testing data: ' + str(ncorrect/i))
