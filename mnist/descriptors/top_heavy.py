import numpy as np
import pdb
# authors: Martin Spanel

def get_features(X):
    pixels = X
    height, width = pixels.shape
    top = int(round(np.sum(pixels[:int(height/2), :])))
    features = np.ndarray.flatten(np.zeros((height,width)))
    features[top] = 1
    return features

"""
success rate on testing data via perceptron on 20 epochs: 0.15311531153115313
[[273   3  46 116   9 224  36  65 119  89]
 [ 17 428  66  35 276  14 103  81  29  86]
 [148  61  53 111  66 181  31 104 127 150]
 [223  30  44 115  50 216  39  80  99 114]
 [106  91  59  83 121  96  45 115 117 149]
 [159  32  59 100  40 151  38  77 126 110]
 [115  68  66  73 109 117  39  87 136 148]
 [153  39  62 120  84 178  40  92 118 142]
 [234  12  38 117  25 217  29  82 118 102]
 [146  30  61  95  75 174  39 100 148 141]]
"""