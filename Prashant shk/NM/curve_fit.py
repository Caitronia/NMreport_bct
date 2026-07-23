import numpy as np

x = np.array([1, 2, 3, 4, 6])
y = np.array([5, 15, 45, 135, 1215])

Y = np.log10(y)
n = len(x)

b = (n*np.sum(x*Y) - np.sum(x)*np.sum(Y)) / (n*np.sum(x*x) - (np.sum(x))**2)
a = (np.sum(Y) - b*np.sum(x)) / n

A = 10**a
B = 10**b

print(f"y = {A:.4f}({B:.4f})^x")
