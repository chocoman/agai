import numpy as np
import pdb
# authors: Samuel Soukup

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges = np.round(X[:,2:]) - np.round(X[:,:height-2])
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
