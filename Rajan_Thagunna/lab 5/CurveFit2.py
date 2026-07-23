
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 7, 10, 12])

n = len(x)

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x*x) - (np.sum(x))**2)
b = (np.sum(y) - a*np.sum(x))/n

print("Equation of best fit:")
print(f"y = {a:.4f}x + {b:.4f}")