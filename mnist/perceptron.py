import numpy as np
import mnist
import pdb
from descriptors import *
import sys

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


    def train(self, get_features, nepochs,meta_epoch = (10,1,0.1,0.1,0.1)):
        self.nfeatures = len(get_features(self.trX[0]))
        # self.w[f, c] is score for class c if feature f is detected
        self.w = np.zeros((self.nfeatures, self.NCLASSES))
        nsamples = self.trX.shape[0]
        #Adjusting the learning rate every 8 epochs
        all_features = np.zeros((nsamples, self.nfeatures))
        print('recognizing features...')
        for i in range(nsamples):
            all_features[i,:] = get_features(self.trX[i])
        print('features recognized')
        for k in range(nepochs):
            self.learning_rate = meta_epoch[k]
            self.test(get_features)
            print ("Learning rate now set to " + str(self.learning_rate))
            for epoch in range(nepochs):
                nerrors = 0            
                for i in range(nsamples):                
                    image_class = self.trY[i]
                    # features = get_features(self.trX[i])
                    features = all_features[i,:]
                    predicted_class = self.classify(features)
                    if predicted_class != image_class:
                        nerrors += 1
                        # self.w[:,image_class] zvysit tam kde jsou jednicky
                        self.w[:,image_class] += features * self.learning_rate
                        # self.w[:,predicted_class] snizit tam kde jsou jednicky
                        self.w[:,predicted_class] -= features * self.learning_rate
                        # TODO update weights to predict better next time\
                    if (i % 200 == 0):
                        sys.stdout.flush()
                        sys.stdout.write(' image {} error {}\r'.format(i, nerrors/(i+1)))
                print('training errors: ' + str(nerrors/nsamples))
        

    def test(self, get_features):
        ncorrect = 0
        confusion = np.zeros((self.NCLASSES, self.NCLASSES), np.int32)

        for i in range(self.teX.shape[0]):
            features = get_features(self.teX[i])
            prediction = self.classify(features)
            confusion[self.teY[i], prediction] += 1
            if (prediction == self.teY[i]):
                ncorrect += 1
        print('success rate on testing data: ' + str(ncorrect/i))
        print(confusion)
