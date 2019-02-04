import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
cactus = ["hugs" for _ in range(n)]

for i in range(n): 
  cactus[i] = list(map(int, list(input().strip())))
for i, row in enumerate(cactus): 
  if sum(row): 
    highest = n - i - 1
    break

cactus = cactus[::-1]

elevator = 0
ans = -1
for floor in range(n): 
  if sum(cactus[floor]): 
    ans += 1
    d = 0 
    new = 0
    for i, room in enumerate(cactus[floor]): 
      if room: 
        if abs(elevator - i) > d: 
          d = abs(elevator - i)
          new = i
    ans += d 

    if floor != highest: 
      if m + 2 - new > new: 
        ans += new
        elevator = 0 
      else: 
        ans += m + 1 - new
        elevator = m + 1
if ans == -1: 
  ans = 0
print ans