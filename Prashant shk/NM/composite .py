def func(x):
    return x**2

lb = 0
ub = 2
n = 6
h = (ub - lb) / n

total = func(lb) + func(ub)
for i in range(1, n):
    total += 2 * func(lb + i*h)

result = h * total / 2
print("Integral =", result)
