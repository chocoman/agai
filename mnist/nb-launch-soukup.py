import numpy as np
import mnist
import pdb
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges, soukup_nwhite,edges90, edges180, edges270, nedges
from nb import nb_mnist

def get_features(X):
    return np.concatenate((
        #white_features.get_features(X),
        #black_features.get_features(X),
        #nwhite_features.get_features(X),
        #soukup_nwhite.get_features(X)
        # top_heavy.get_features(X),
        edges.get_features(X),
        edges90.get_features(X),
        edges180.get_features(X),
        edges270.get_features(X),
        #nedges.get_features(X),

    ))

classifier = nb_mnist()
classifier.train(get_features)
classifier.test(get_features)
