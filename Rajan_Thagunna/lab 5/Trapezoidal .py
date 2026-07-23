def f(x):
    return x**2
a = 0
b = 4
n = 4
h = (b-a)/n
s = f(a)+f(b)
for i in range(1,n):
    s += 2*f(a+i*h)
ans = h*s/2
print("Integral =", ans)