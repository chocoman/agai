import numpy as np
# authors: Martin Spanel

def get_features(X):
    pixels = np.ndarray.flatten(X)
    return np.round(1-pixels)
