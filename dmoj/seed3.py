import sys
input = sys.stdin.readline

i = int(input())
n = int(input())
j = int(input())

stations = [0 for x in xrange(i + 1)]
for _ in xrange(j):
    xi, xf, k = map(int, input().split())
    stations[xi - 1] += k
    stations[xf] -= k

a = 1 if stations[0] < n else 0

for x in xrange(1, i):
    stations[x] += stations[x - 1]
    if stations[x] < n:
        a += 1

print a
