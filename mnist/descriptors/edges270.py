import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges = np.round(X[:,:height-2]) - np.round(X[:,2:])
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
