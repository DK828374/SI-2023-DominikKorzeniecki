import numpy as np

# funkcja aktywacji
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# funkcja AND
def AND(x1, x2):
    X = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    return step_function(np.dot(w, X) + b)

# funkcja NOT
def NOT(x):
    X = np.array([x])
    w = np.array([-1])
    b = 0.5
    return step_function(np.dot(w, X) + b)

print(AND(1, 1)) # powinno zwrócić 1
print(NOT(0))  # powinno zwrócić 1
print(NOT(1))  # powinno zwrócić 0
