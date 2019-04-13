import sys, math
input = sys.stdin.readline

n = int(input())

eggs = [] 

ans = ""
ap = 0 
gp = 0
for i in xrange(n): 
  a, g = map(int, input().split())
  pls = abs((ap + a) - gp)
  if pls > 500 and abs(ap - (gp + g)) > 500:
    ans = -1 
    break 

  if pls > 500: 
    gp += g 
    ans += "G"
  else: 
    ap += a
    ans += "A"
print ans