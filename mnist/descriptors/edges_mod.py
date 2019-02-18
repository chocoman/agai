import numpy as np
import pdb
# authors: Ondřej Maceška

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges = X[2:,:] - X[:width-2,:]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    return np.ndarray.flatten(ret)