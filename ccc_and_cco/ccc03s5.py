import sys
from heapq import heappush, heappop
input = sys.stdin.readline

c, r, d, = map(int, input().split())

cactus = [[] for x in xrange(c + 1)]

for i in range(r):
    x, y, w = map(int, input().split())
    cactus[x].append((y, w))
    cactus[y].append((x, w))

dests = [0] * d
for i in range(d):
    dests[i] = int(input())

q = [(1, 0)]
paths = [-1 for x in range(c + 1)]
paths[1] = 0

while q:
    node, w = heappop(q)
    for dest, weight in cactus[node]:
        if paths[dest] >= weight:
            continue
        paths[dest] = weight
        heappush(q, (dest, weight))

ans = 1 << 30
for dest in dests:
    ans = min(ans, paths[dest])
print ans
