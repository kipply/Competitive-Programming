import sys, math, os
from fractions import gcd
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
counts = {}
for x in a: 
  if x not in counts: 
    counts[x] = 1 
  else: 
    counts[x] += 1

ans = []
while len(ans) < n:
  x = max(counts.keys())
  counts[x] -= 1
  if counts[x] == 0: 
    counts.pop(x)
  for y in ans:
    d = gcd(x, y)
    counts[d] -= 2
    if counts[d] == 0: 
      counts.pop(d)
  ans.append(x)

if any([counts[x] < 0 for x in counts.keys()]): 
  print -1
else: 
  print " ".join(map(str, ans))