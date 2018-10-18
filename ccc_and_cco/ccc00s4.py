# Essentially the "Coin Change" problem
from sys import stdin
def f(clubs, m, V):
    t = ["fasterpls"] * (V + 1)
    t[0] = 0
    for i in range(1, V + 1):
        for j in range(m):
            if clubs[j] <= i:
                s = t[i - clubs[j]]
                if s != "fasterpls" and s + 1 < t[i]:
                    t[i] = s + 1
    return t[V]
d = int(stdin.readline())
n = int(stdin.readline())
c = [0] * n
for i in range(n):
    c[i] = int(stdin.readline())
if f(c, n, d) == "fasterpls":
    print "Roberta acknowledges defeat."
else:
    print "Roberta wins in " + str(f(c, n, d)) + " strokes."
