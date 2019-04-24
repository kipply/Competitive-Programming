import sys
input = sys.stdin.readline 

hugs = input().strip() 
cute = input().strip()
cactus = input().strip()
n = int(input()) 

print(hugs.count(cute))

curr = 0
for i in range(n): 
  curr = hugs.index(cute, curr) + len(cute)

hugs = hugs[:curr - len(cute)] + hugs[curr - len(cute):].replace(cute, cactus, 1)

print hugs
# print ans
# 
# 
# 