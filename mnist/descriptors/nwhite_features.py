import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = np.round(np.ndarray.flatten(X))
    nwhite = int(np.sum(pixels))
    features = np.zeros(len(pixels))
    features[0:nwhite] = 1
    return features
