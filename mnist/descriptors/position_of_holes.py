import numpy as np
import pdb
from visualize import visualize_matrix

# authors: Samuel Soukup
from graph import graph
def get_features(X, weight = 1000):
    pixels = X
    g = graph.Graph(np.round(X))
    unreachable = g.pozice_nedosazitelnych(0)
    
    return unreachable
