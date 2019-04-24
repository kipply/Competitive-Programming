import sys
input = sys.stdin.readline 

hugs = input().strip() 
cute = input().strip()
cactus = input().strip()
n = int(input()) 


count = 0
found = 0; 
for i in range(len(hugs) - len(cute) + 1):
  f = True
  for j in range(len(cute)): 
    if hugs[i + j] != cute[j]: 
      f = False
  if f: 
    count += 1
    if (count == n): 
      found = i

print count
hugs = hugs[:found] + cactus + hugs[found + len(cute):] 

print hugs
