import numpy as np
import pdb
# authors: Jirka Láska <3

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges = X[:,2:] - X[:,:height-2]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)

