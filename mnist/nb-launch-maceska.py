import numpy as np
import mnist
import pdb
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges, edges_mod, edges2
from nb import nb_mnist
#Ondřej Maceška
def get_features(X):
    return np.concatenate((
        #white_features.get_features(X),
        #black_features.get_features(X),
        # nwhite_features.get_features(X),
        # random_features.get_features(X),
        #top_heavy.get_features(X),
        # ones.get_features(X),
        #edges.get_features(X),
        edges2.get_features(X),
        #edges_mod.get_features(X), 
    ))

classifier = nb_mnist()
classifier.train(get_features)
classifier.test(get_features)
