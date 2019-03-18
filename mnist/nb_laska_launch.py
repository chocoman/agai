import numpy as np
import mnist
import pdb
from descriptors import edges, hedges, black_features, joints, connected
from nb import nb_mnist
from perceptron import perceptron_mnist

def get_features(X):
    return np.concatenate((
        edges.get_features(X),
        hedges.get_features(X),
        black_features.get_features(X),
        connected.get_features(X,500),
    ))

#classifier = nb_mnist()
classifier = perceptron_mnist(4)
classifier.train(get_features,3)
classifier.test(get_features)
