import numpy as np
import pdb
# authors: Ondřej Maceška

def get_features(X):
    pixels = X
    offsetleft = 2
    offsetright = 26
    height, width = pixels.shape
    edges = X[2:,offsetleft:] - X[:height-2,:offsetright]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)
