import numpy as np
import mnist
import pdb
from descriptors import *

class nb_mnist:

    def __init__(self):
        self.trX, self.trY, self.teX, self.teY = mnist.load_data(
                one_hot=False, flatten=False)
        self.NCLASSES = 10

    def classify(self, features):
        log_likelihoods = np.zeros((self.NCLASSES,))
        for c in range(self.NCLASSES):
            for i in range(self.nfeatures):
                if (features[i]):
                    log_likelihoods[c] += self.log_probability[i,c]
        return np.argmax(log_likelihoods + self.log_priors)

    def train(self, get_features):
        self.nfeatures = len(get_features(self.trX[0])) # zjistime pocet priznaku zavolanim funkce get_features
        # probability[i][j] is P(class == j, feature[j] == True)
        probability = np.zeros((self.nfeatures, self.NCLASSES))
        priors = np.zeros((self.NCLASSES)) # pravdepodobnost jednotlivych trid bez ohledu na priznaky
        
        nsamples = self.trX.shape[0]
        for i in range(nsamples):
            image_class = self.trY[i]
            priors[image_class] += 1
            features = get_features(self.trX[i])
            probability[:,image_class] += features
        self.log_probability = np.log((probability + 0.000001)/nsamples)
        self.log_priors = np.log((priors + 0.000001)/nsamples)

    def test(self, get_features):
        ncorrect = 0
        confusion = np.zeros((self.NCLASSES, self.NCLASSES))
        for i in range(self.teX.shape[0]):
            features = get_features(self.teX[i])
            prediction = self.classify(features)
            confusion[self.teY[i], prediction] += 1
            if (prediction == self.teY[i]):
                ncorrect += 1
            if (i % 100 == 0 and i > 0):
                print(ncorrect/i)
        print(confusion)
        print(ncorrect/i)
