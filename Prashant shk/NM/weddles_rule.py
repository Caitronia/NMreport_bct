def func(x):
    return x**3

lb = 0
ub = 6
h = (ub - lb) / 6

result = (3*h/10) * (func(lb) + 5*func(lb+h) + func(lb+2*h) + 6*func(lb+3*h) +
                      func(lb+4*h) + 5*func(lb+5*h) + func(ub))

print("Integral =", result)
