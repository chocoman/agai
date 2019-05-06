import numpy as np
import mnist
import pdb

def feed_forward(X, weights):
    a = [X]
    for w in weights:
        a.append(np.maximum(a[-1].dot(w),0))
    return a

def grads(X, Y, weights):
    grads = np.empty_like(weights)
    a = feed_forward(X, weights)
    delta = a[-1] - Y
    grads[-1] = a[-2].T.dot(delta)
    for i in range(len(a)-2, 0, -1):
        delta = (a[i] > 0) * delta.dot(weights[i].T)
        grads[i-1] = a[i-1].T.dot(delta)
    return grads / len(X)


def train(trX, trY, teX, teY, weights, num_epochs=3, batch_size=20, learn_rate=0.1):
    for i in range(num_epochs):
        for j in range(0, len(trX), batch_size):
            X, Y = trX[j:j+batch_size], trY[j:j+batch_size]
            weights -= learn_rate * grads(X, Y, weights)
        prediction = np.argmax(feed_forward(teX, weights)[-1], axis=1)
        print(str(i) + ': ' + str(np.mean(prediction == np.argmax(teY, axis=1))))
