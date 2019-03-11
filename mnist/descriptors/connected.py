import numpy as np
import pdb
from visualize import visualize_matrix

# authors: Martin Spanel
from graph import graph
def get_features(X, weight = 1000):
    pixels = X
    g = graph.Graph(X)
    nunreachable = g.BFS(0)
    ret = np.zeros(weight)
    
    if (nunreachable != 0):
      # visualize_matrix(X)
      ret += 0
    return ret
