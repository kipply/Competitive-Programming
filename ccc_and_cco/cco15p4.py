# Solution _probably_ passes, will refactor into C++

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
from heapq import heappush, heappop

g = [[] for x in range(n)]
cars = []
for i in range(n):
  g[i] = list(input())
  for j in range(m):
    if g[i][j] in "NSWE":
      heappush(cars, (0, i, j, g[i][j]))
      g[i][j] = 0

ans = []
while cars:
  t, r, c, d = cars[0]
  f = 1
  if d == "N":
    for j in range(r - 1, -1, -1):
      if g[j][c] != ".":
        f = 0
        g[r][c] += g[j][c] if g[j][c] else 1
  elif d == "S":
    for j in range(r + 1, n):
      if g[j][c] != ".":
        f = 0
        g[r][c] += g[j][c] if g[j][c] else 1
  elif d == "E":
    for j in range(c + 1, m):
      if g[r][j] != ".":
        f = 0
        g[r][c] += g[r][j] if g[r][j] else 1
  else:
    for j in range(c - 1, -1, -1):
      if g[r][j] != ".":
        f = 0
        g[r][c] += g[r][j] if g[r][j] else 1

  if f:
    g[r][c] = '.'
    ans.append(heappop(cars))
  else:
    t, x, y, z = heappop(cars)
    heappush(cars, (g[r][c], x, y, z))
for x in ans:
  sys.stdout.write("("+str(x[1])+","+str(x[2])+")\n")
