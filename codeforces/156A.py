import sys
input = sys.stdin.readline 

s = input().strip()
u = input().strip()

diffs = 0 

for i in range(max(len(s), len(u))): 
  diffs = max(
    sum([s[i:][x] == u[x] for x in range(min(len(s[i:]), len(u)))]),
    sum([s[x] == u[i:][x] for x in range(min(len(s), len(u[i:])))]),
    diffs
  )
print len(u) - diffs