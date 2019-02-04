import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
cactus = [input().strip() for _ in range(n)]

max_floor = 0
for i, floor in enumerate(cactus): 
  if '1' in floor: 
    max_floor = n - i - 1
    break

cactus = cactus[::-1]

l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
ans = 1 << 30
for i, floor in enumerate(cactus):
  if '1' in floor:
    l[i] = floor.index('1') 
    r[i] = floor.rfind('1')

def bf(curr, floor, distance):
  global ans
  if floor == max_floor: 
    distance += max(abs(curr - l[floor]), abs(curr - r[floor]))
    ans = min(ans, distance)
    return 
  if '1' not in cactus[floor]: 
    bf(curr, floor + 1, distance + 1)
    return
  if curr: 
    bf(0, floor + 1, distance + abs(curr - l[floor]) + l[floor] + 1)
    bf(m + 1, floor + 1, distance + abs(curr - l[floor]) + m + 1 - l[floor] + 1)
  else: 
    bf(0, floor + 1, distance + abs(curr - r[floor]) + r[floor] + 1)
    bf(m + 1, floor + 1, distance + abs(curr - r[floor]) + m + 1 - r[floor] + 1)
    
bf(0, 0, 0)
print ans