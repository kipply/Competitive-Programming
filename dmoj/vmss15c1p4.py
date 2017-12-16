import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t, n, m, g = map(int, input().split())
food_basics = [int(input()) for x in range(g)]

cactus = [[] for x in range(n + 1)]
for i in range(m):
    a, b, l = map(int, input().split())
    cactus[a].append((b, l))

q = [(0, 0)]
d = [-1] * (n + 1)
while q:
    dist, node = heappop(q)
    if d[node] != -1:
        continue
    d[node] = dist
    if dist > t:
        continue
    for dest, add in cactus[node]:
        heappush(q, (dist + add, dest))

ans = 0
for food_basic in food_basics:
    if d[food_basic] <= t and d[food_basic] != -1:
        ans += 1

print ans
