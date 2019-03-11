import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    offsetleft = 2
    offsetright = 26
    height, width = pixels.shape
    edges = X[:,offsetleft:] - X[:,:offsetright]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
