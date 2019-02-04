import numpy as np
import mnist
import pdb
from descriptors import black_features, white_features,nwhite_features
NCLASSES = 10

def get_features(X):
    return np.concatenate((
        white_features.get_features(X),
        black_features.get_features(X),
        nwhite_features.get_features(X),
    ))

def classify(features):
    likelihoods = np.ones((10,))
    for c in range(NCLASSES):
        for i in range(nfeatures):
            if (features[i]):
                likelihoods[c] += log_probability[i,c]
    return np.argmax(likelihoods)

trX, trY, teX, teY = mnist.load_data(one_hot=False, flatten=False)

# probability[i][j] is P(class == j, feature[j] == True)
nfeatures = len(get_features(trX[0]))
probability = np.zeros((nfeatures, NCLASSES))

for i in range(trX.shape[0]):
    image_class = trY[i]
    features = get_features(trX[i])
    probability[:,image_class] += features
log_probability = np.log(probability + 0.000001)

ncorrect = 0
for i in range(teX.shape[0]):
    features = get_features(teX[i])
    prediction = classify(features)
    if (prediction == teY[i]):
        ncorrect += 1
    if (i % 100 == 0 and i > 0):
        print(ncorrect/(i+0.001))


pdb.set_trace()
