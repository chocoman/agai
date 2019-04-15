import numpy as np
import mnist
import pdb
from descriptors import black_features, nwhite_features, top_heavy, edges, edges90, edges180, edges270, bot_heavy, joints, connected, position_of_holes
from nb import nb_mnist
from perceptron import perceptron_mnist

def get_features(X):
    return np.concatenate((
        black_features.get_features(X),
        #nwhite_features.get_features(X),
        top_heavy.get_features(X),
        edges.get_features(X),        
        edges90.get_features(X),
        edges180.get_features(X),
        edges270.get_features(X),
        bot_heavy.get_features(X),
        joints.get_features(X),
        #connected.get_features(X),
        position_of_holes.get_features(X),

    ))

classifier = perceptron_mnist(10)
classifier.train(get_features,(30,30,30,30),(100,10,1,0.1,0.1))
classifier.test(get_features)