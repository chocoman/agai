import numpy as np
# authors: Samuel & Georg Soukupovi

def get_features(X):
    edges = np.abs(np.diff(X, axis=1)) > 0
    return np.round(np.ndarray.flatten(np.ndarray.flatten(X)))