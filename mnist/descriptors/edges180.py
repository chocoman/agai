import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges =  X[:width-2,:] - X[2:,:]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)