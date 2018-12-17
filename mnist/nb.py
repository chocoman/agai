import numpy as np
import mnist
import pdb

NCLASSES = 10
NFEATURES = 28 * 28 * 2

def get_features(X):
    # return np.round(X)
    return np.concatenate((np.round(X), np.round(1-X)))

def classify(features):
    likelihoods = np.ones((10,))
    for c in range(NCLASSES):
        for i in range(NFEATURES):
            if (features[i]):
                likelihoods[c] *= probability[i,c]
    return np.argmax(likelihoods)

trX, trY, teX, teY = mnist.load_data(one_hot=False, flatten=True)

# probability[i][j] is P(class == j, feature[j] == True)
probability = np.zeros((NFEATURES, NCLASSES))

for i in range(trX.shape[0]):
    image_class = trY[i]
    features = get_features(trX[i])
    probability[:,image_class] += features

ncorrect = 0
for i in range(teX.shape[0]):
    features = get_features(teX[i])
    prediction = classify(features)
    if (prediction == teY[i]):
        ncorrect += 1
    print(ncorrect/(i+0.001))


pdb.set_trace()
