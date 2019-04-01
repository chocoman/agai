import numpy as np
import mnist
import pdb
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges, connected
from nb import nb_mnist
from perceptron import perceptron_mnist

def get_features(X):
    return np.concatenate((
        # white_features.get_features(X),
        # black_features.get_features(X),
        # nwhite_features.get_features(X),
        # random_features.get_features(X),
        # top_heavy.get_features(X),
        # ones.get_features(X),
        edges.get_features(X),
        # connected.get_features(X, 1000),
        # random_features.get_features(X),
    ))

# classifier = nb_mnist()
classifier = perceptron_mnist(4)
filename = input('load perceptron from file (leave empty to skip):')
if filename != '':
    classifier.load(filename)
classifier.train(get_features,1)
classifier.test(get_features)
