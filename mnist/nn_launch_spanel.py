import minimalist_nn
import numpy as np
import mnist
from descriptors import white_features, black_features, nwhite_features, random_features, top_heavy, ones, edges, connected

def get_features(X):
    return np.concatenate((
        black_features.get_features(X),
        edges.get_features(X),
        # connected.get_features(X, 1000),
    ))


trX, trY, teX, teY = mnist.load_data(one_hot=True, flatten=False)

nfeatures = len(get_features(trX[0]))
nsamples = trX.shape[0]
ntests = teX.shape[0]
tr_features = np.zeros((nsamples, nfeatures))
te_features = np.zeros((ntests, nfeatures))

print('recognizing features...')
for i in range(nsamples):
    tr_features[i,:] = get_features(trX[i])
for i in range(ntests):
    te_features[i,:] = get_features(teX[i])
print('features recognized')

weights = [np.random.randn(*w) * 0.1 for w in [(nfeatures, 200), (200, 10)]]
minimalist_nn.train(tr_features, trY, te_features, teY, weights,
                    num_epochs=100)
