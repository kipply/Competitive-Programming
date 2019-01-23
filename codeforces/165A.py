import sys
input = sys.stdin.readline

n = int(input())
points = [] 
cute_x = {}
cute_y = {}

for i in range(n): 
  x, y = map(int, input().split())
  if x in cute_x.keys(): 
    cute_x[x].append(y)
  else: 
    cute_x[x] = [y]

  if y in cute_y.keys(): 
    cute_y[y].append(x)
  else: 
    cute_y[y] = [x]
 
  points.append((x, y))

ans = 0
for x, y in points: 
  if max(cute_y[y]) > x and min(cute_y[y]) < x and max(cute_x[x]) > y and min(cute_x[x]) < y: 
    ans += 1

print ans