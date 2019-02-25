import numpy as np
# authors: Martin Spanel

def get_features(X):
    return np.round(np.ndarray.flatten(0.6 - X))
