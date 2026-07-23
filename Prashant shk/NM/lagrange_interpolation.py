def interpolate(xs, ys, x0):
    n = len(xs)
    y0 = 0
    for i in range(n):
        term = 1
        for j in range(n):
            if i != j:
                term *= (x0 - xs[j]) / (xs[i] - xs[j])
        y0 += term * ys[i]
    return y0

xs = [1, 2, 5]
ys = [3, 8, 26]
x0 = 3

print("Interpolated value =", interpolate(xs, ys, x0))
