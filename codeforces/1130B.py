import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
tiers = defaultdict(list) 
for i in range(n * 2): 
  tiers[a[i]].append(i)

ans = 0 
for _ in range(2): 
  pos = 0
  c = 1 
  while c < n + 1: 
    lo = 1 << 30 
    next_pos = 0 
    for i in range(len(tiers[c])): 
      if abs(tiers[c][i] - pos) < lo: 
        lo = abs(tiers[c][i] - pos)
        next_pos = tiers[c][i]

    tiers[c].remove(next_pos)
    pos = next_pos
    c += 1 
    ans += lo

print ans 