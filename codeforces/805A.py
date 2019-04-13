import sys, math, os
input = sys.stdin.readline

l, r = map(int, input().split())
counts = [(r - l) / 2, 0]
if not r % 2 or not l % 2:
  counts[0] += 1

if l % 2: 
  s = l 
else: 
  s = l + 1

if abs(l - r) < 100: 
  for x in range(s, r + 1, 2): 
    if not x % 2: 
      counts[0] += 1 
    if not x % 3: 
      counts[1] += 1 
  if l == r: 
    print l
  elif counts[1] > counts[0]: 
    print 3 
  else: 
    print 2
else: 
  print 2