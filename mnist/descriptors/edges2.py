import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    offsetleft = 3
    offsetright = 25
    height, width = pixels.shape
    edges = X[3:,offsetleft:] - X[:height-3,:offsetright]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
