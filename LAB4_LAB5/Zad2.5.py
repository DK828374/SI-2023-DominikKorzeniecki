import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


X = np.array([[0.6, 0.1], [0.2, 0.3]])
y = np.array([[1], [0]])

weights1 = np.array([[0.1, -0.2], [0, 0.2], [0.3, -0.4]])
weights2 = np.array([[-0.4, 0.1, 0.6], [0.2, -0.1, -0.2]])

learning_rate = 0.1
for i in range(40000):
    r1 = sigmoid(np.dot(X, weights1.T))
    r2 = sigmoid(np.dot(r1, weights2.T))

    r2e = y - r2
    r2g = r2e * sigmoid_derivative(r2)

    r1e = r2g.dot(weights2)
    r1g = r1e * sigmoid_derivative(r1)

    weights2 += r1.T.dot(r2g).T * learning_rate
    weights1 += X.T.dot(r1g).T * learning_rate

print("Wynik:")
print(r2)
