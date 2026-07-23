import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 8, 11, 14])

n = len(x)
m = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x*x) - (np.sum(x))**2)
c = (np.sum(y) - m*np.sum(x)) / n

print("Equation of best fit:")
print("y =", m, "x +", c)
