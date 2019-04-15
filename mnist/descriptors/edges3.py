import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    offsetleft = 4
    offsetright = 24
    height, width = pixels.shape
    edges = X[4:,offsetleft:] - X[:height-4,:offsetright]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
