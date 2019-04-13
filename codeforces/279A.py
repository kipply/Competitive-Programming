import sys, math
input = sys.stdin.readline

X, Y = map(int, input().split())

x, y = 0, 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

d = 0 
ans = 0
m = 1 
while not (x == X and y == Y): 
  print x, y
  ans += 1
  x += directions[d][0] * m
  y += directions[d][1] * m
  d += 1
  if d > 3: 
    d = 0 
  if not (d) % 2: 
    m += 1

  if x > 100 or x < -100: break

print ans