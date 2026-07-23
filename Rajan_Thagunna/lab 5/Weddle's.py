def f(x):
    return x**2
a = 0
b = 6
h = (b-a)/6
ans = (3*h/10)*(f(a)+5*f(a+h)+f(a+2*h)+6*f(a+3*h)+f(a+4*h)+5*f(a+5*h)+f(b))
print("Integral =", ans)