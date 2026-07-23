def lagrange(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j])/(x[i]-x[j])
        yp += p*y[i]
    return yp

x = [1, 3, 4]
y = [2, 10, 17]

xp = 2
print("Interpolated value =", lagrange(x,y,xp))
