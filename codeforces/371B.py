import sys, math
input = sys.stdin.readline

x, y = map(int, input().split())
cactus_x = [0, 0, 0]
cactus_y = [0, 0, 0]

for i, bloop in enumerate([2, 3, 5]): 
  while not x % bloop: 
    x /= bloop
    cactus_x[i] += 1 
  while not y % bloop: 
    y /= bloop
    cactus_y[i] += 1 

# print cactus_x, cactus_y
ans = 0
for bloop in range(3):
  ans += abs(cactus_x[bloop] - cactus_y[bloop])

if not x == y: 
  ans = -1 

print ans