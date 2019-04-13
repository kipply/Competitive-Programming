import sys, math, os
input = sys.stdin.readline

n, m = map(int, input().split())
hor = input()
vert = input()

v = [[0 for _ in range(m)] for _ in range(n)]


def solve(r, c): 
  global v 
  if v[r][c]: return 
  v[r][c] = 1
  if hor[r] == ">": 
    if c + 1 < m: 
      solve(r, c + 1)
  else: 
    if c - 1 >= 0: 
      solve(r, c - 1)

  if vert[c] == "v": 
    if r + 1 < n: 
      solve(r + 1, c)
  else: 
    if r - 1 >= 0: 
      solve(r - 1, c)

ans = []
for i in range(n): 
  for j in range(m): 
    v = [[0 for _ in range(m)] for _ in range(n)]

    solve(i, j)

    if any(sum(row) < m for row in v): 
      ans.append(0)
    else: 
      ans.append(1) 
if all(ans): 
  print "YES" 
else: 
  print "NO"