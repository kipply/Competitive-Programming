import sys, math, os
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7 + 1)

n, m = map(int, input().split())

cactus = [[] for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]

def kill(n): 
  q = [n]
  v[n] = 1
  while q: 
    nn = q.pop(0)
    for x in cactus[nn]: 
      if not v[x]: 
        v[x] = 1
        q.append(x)

for _ in range(m):
  x, y = map(int, input().split())
  cactus[x].append(y)
  cactus[y].append(x)

ans = 0
for x in range(1, n + 1): 
  if len(cactus[x]) != 2 and not v[x]: 
    kill(x)

for x in range(1, n + 1): 
  if len(cactus[x]) == 2 and not v[x]: 
    kill(x)
    ans += 1

print ans