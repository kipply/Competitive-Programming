from sys import stdin
n, q = map(int, stdin.readline().split())
psa = [0] + map(int, stdin.readline().split())
for i in xrange(1, n + 1):
    psa[i] += psa[i - 1]
t = psa[-1]
for i in xrange(q):
    a, b = map(int, stdin.readline().split())
    print t - psa[b] + psa[a - 1]
