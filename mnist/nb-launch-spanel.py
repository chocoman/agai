import numpy as np
import mnist
import pdb
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges
from nb import nb_mnist

def get_features(X):
    return np.concatenate((
        # white_features.get_features(X),
        # black_features.get_features(X),
        # nwhite_features.get_features(X),
        # random_features.get_features(X),
        # top_heavy.get_features(X),
        # ones.get_features(X),
        edges.get_features(X),
    ))

classifier = nb_mnist()
classifier.train(get_features)
classifier.test(get_features)
