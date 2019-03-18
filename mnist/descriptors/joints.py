import numpy as np
import pdb
from visualize import visualize_matrix

# authors: Samuel & Georg Soukupovi

def get_features(X):
    edges = np.abs(np.diff(X, axis=0))+np.abs(np.diff(X,axis=0))
    #visualize_matrix(edges)
    #visualize_matrix(X)
    #print(edges.shape)
    #pdb.set_trace()
    return np.ndarray.flatten(np.ndarray.flatten(X))