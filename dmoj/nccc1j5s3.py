def f(N):
    threshold = N * (N - 1) / 2

    lo = 1
    hi = N
    if n < 5:
        return 1
    while lo < hi:
        g = (hi + lo + 1) / 2
        if g * (g - 1) > threshold:
            hi = g - 1
        else:
            lo = g
    return N - lo
n = int(input())

print f(n)