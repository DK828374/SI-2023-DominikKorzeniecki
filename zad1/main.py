import numpy as np
from numpy import loadtxt


# lines = loadtxt("fertilityDiagnosis.txt", comments="#", delimiter=" ", unpack=True)
# others = loadtxt("fertilityDiagnosis-type.txt", comments="#", delimiter=" ", unpack=True)
#
# diagnoza = np.array([lines],[others])
# print(diagnoza.shape)

a = open("fertilityDiagnosis.txt")
b = open("fertilityDiagnosis-type.txt")
contents = a.read()
col = b.read()
print(contents)
arrc = np.array([col])
arr = np.array([contents])

#
# print(arrc)
# print(arrc.shape)