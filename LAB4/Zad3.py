import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def xor_perceptron(x1, x2):
    # Warstwa ukryta
    input_layer = np.array([x1, x2])
    weights_hidden = np.array([[20, -20], [-20, 20]])
    biases_hidden = np.array([-10, 30])
    hidden_output = sigmoid(np.dot(input_layer, weights_hidden) + biases_hidden)

    # Warstwa wyjściowa
    weights_output = np.array([20, 20])
    bias_output = np.array([-30])
    output = sigmoid(np.dot(hidden_output, weights_output) + bias_output)

    return output

# Testowanie sieci dla różnych przypadków XOR
print(xor_perceptron(0, 0))  # 0 XOR 0 = 0
print(xor_perceptron(0, 1))  # 0 XOR 1 = 1
print(xor_perceptron(1, 0))  # 1 XOR 0 = 1
print(xor_perceptron(1, 1))  # 1 XOR 1 = 0
