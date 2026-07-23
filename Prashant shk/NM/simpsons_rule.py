def func(x):
    return x**2

lb = 0
ub = 8
n = 8
h = (ub - lb) / n

total = func(lb) + func(ub)
for i in range(1, n):
    if i % 2 == 0:
        total += 2 * func(lb + i*h)
    else:
        total += 4 * func(lb + i*h)

result = h * total / 3
print("Integral =", result)
