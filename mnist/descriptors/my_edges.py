import numpy as np
import pdb
# authors: Jachym Sulman
from visualize import visualize_matrix

def get_features(X):
    pixels = X
    height, width = pixels.shape
    ofdown = 3
    ofup = height - ofdown
    ofright = 2
    ofleft = width - ofright
    edges = X[ofdown:,ofright:] - X[:ofup,:ofleft]
    ret = np.zeros(edges.shape)
    ret[edges > 0] = 1
    # visualize_matrix(ret)
    # pdb.set_trace()
    return np.ndarray.flatten(ret)