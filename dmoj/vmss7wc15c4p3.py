# somehow spfa just goes fast.
import sys

from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cactus = [[] for x in xrange(n)]
for i in xrange(m):
  a, b, t = map(int, input().split())
  cactus[a].append([b, t])
  cactus[b].append([a, t])

d = [0] * n
q = deque([(0, 0)])
while q:
  node, dist = q.popleft()
  for no, di in cactus[node]:
    if dist + di < d[no] or not d[no]:
      d[no] = dist + di
      q.append([no, d[no]])

q = deque([(n - 1, 0)])
dd = [0] * n

while q:
  node, dist = q.popleft()
  for no, di in cactus[node]:
    if dist + di < dd[no] or not dd[no]:
      dd[no] = dist + di
      q.append([no, dd[no]])

d[0] = dd[-1] = 0

print(max(map(sum, zip(d, dd))))
