import numpy as np
import pdb
# authors: Martin Spanel
from visualize import visualize_matrix

def get_features(X):
    pixels = X
    height, width = pixels.shape
    edges = X[2:,:] - X[:height-2,:]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    visualize_matrix(ret)
    return np.ndarray.flatten(ret)
