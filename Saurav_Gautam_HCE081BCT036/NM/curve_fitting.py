import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([3, 9, 27, 81, 243])
Y = np.log10(y)
n = len(x)
B = (n*np.sum(x*Y)-np.sum(x)*np.sum(Y))/(n*np.sum(x*x)-(np.sum(x))**2)
A = (np.sum(Y)-B*np.sum(x))/n

a = 10**A
b = 10**B

print(f"y = {a:.4f}({b:.4f})^x")
