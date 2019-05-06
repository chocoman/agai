import numpy as np
import mnist
import pdb
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges, edges_mod, edges2, edges3, edges_vertical, edges90, edges180, edges270, edges271
from perceptron import perceptron_mnist
#Ondřej Maceška
def get_features(X):
    return np.concatenate((
        white_features.get_features(X),
        black_features.get_features(X),
        nwhite_features.get_features(X),
        #random_features.get_features(X),
        top_heavy.get_features(X),
        #ones.get_features(X),
        edges.get_features(X),
        edges2.get_features(X),
        edges3.get_features(X),
        #edges90.get_features(X),
        edges180.get_features(X),
        edges270.get_features(X),
        #edges271.get_features(X),
        edges_vertical.get_features(X),
        edges_mod.get_features(X), 
    ))

classifier = perceptron_mnist(1)
classifier.train(get_features, 1)
classifier.test(get_features)
