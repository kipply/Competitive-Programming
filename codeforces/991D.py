import sys
input = sys.stdin.readline 

cactus = ["", ""]
cactus[0] = (list(input().strip()))
cactus[1] = (list(input().strip()))

ans = 0 
prev = 0

for i in range(len(cactus[0])): 
  curr = 0
  if cactus[0][i] is "0": 
    curr += 1
  if cactus[1][i] is "0": 
    curr += 1


  if not curr: 
    prev = 0 
  elif curr == 1: 
    if prev == 2: 
      ans += 1
      prev = 0 
    else: 
      prev = 1
  elif curr == 2: 
    if prev == 1: 
      ans += 1 
      prev = 0
    elif prev == 2: 
      ans += 1
      prev = 1 
    elif not prev: 
      prev = 2

print ans