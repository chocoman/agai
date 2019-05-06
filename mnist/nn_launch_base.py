import minimalist_nn
import numpy as np
import mnist

trX, trY, teX, teY = mnist.load_data(flatten=True)
weights = [np.random.randn(*w) * 0.1 for w in [(784, 100), (100, 100), (100, 10)]]

minimalist_nn.train(trX, trY, teX, teY, weights)
