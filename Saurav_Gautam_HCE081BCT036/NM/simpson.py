def f(x):
    return x**2

a = 0
b = 6
n = 6
h = (b-a)/n
s = f(a)+f(b)

for i in range(1,n):
    if i%2==0:
        s += 2*f(a+i*h)
    else:
        s += 4*f(a+i*h)

ans = h*s/3
print("Integral =", ans)
