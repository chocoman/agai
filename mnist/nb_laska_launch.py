import numpy as np
import mnist
import pdb
from descriptors import edges, hedges, black_features, joints, connected, position_of_holes
from nb import nb_mnist
from perceptron import perceptron_mnist

def get_features(X):
    return np.concatenate((
        edges.get_features(X),
        hedges.get_features(X),
        black_features.get_features(X),
        connected.get_features(X,500),
        position_of_holes.get_features(X),
    ))

#classifier = nb_mnist()
classifier = perceptron_mnist(10)
classifier.train(get_features,(30,30,30,30),(100,10,1,0.1,0.1))
classifier.test(get_features)
