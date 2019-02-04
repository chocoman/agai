import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    height, width = pixels.shape
    top = np.sum(pixels[:int(height/2), :])
    bottom = np.sum(pixels[int(height/2):, :])
    top_heavy = False
    return np.array([top_heavy, not top_heavy] )
