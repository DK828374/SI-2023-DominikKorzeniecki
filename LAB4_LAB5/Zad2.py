# funkcja aktywacji
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# perceptron x1 ∧ ¬x2
def x1_and_not_x2(x1, x2):
    w1 = 1
    w2 = 1
    w_bias = -1
    result = w1 * x1 + w2 * (-x2) + w_bias
    return step_function(result)

print(x1_and_not_x2(1, 0))  # powinno zwrócić 1
print(x1_and_not_x2(0, 1))  # powinno zwrócić 0
print(x1_and_not_x2(0, 0))  # powinno zwrócić 0
print(x1_and_not_x2(1, 1))  # powinno zwrócić 0