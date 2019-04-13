import sys, math, os
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
counts = [0 for _ in range(9)]
for x in a: 
  counts[x] += 1
ans = []


for x in range(9): 
  for y in range(counts[x]): 
    c = 0
    a = [x]
    counts[x] -= 1
    for i in range(2, 9): 
      if x * i > 8: break
      if counts[x * i]: 
        counts[x * i] -= 1
        a.append(x * i)
        c += 1
        break
    for i in range(2, 9): 
      if a[-1] * i > 8: break
      if counts[a[-1] * i]: 
        counts[a[-1] * i] -= 1
        a.append(a[-1] * i)
        c += 1
        break
    if c != 2: 
      ans = -1 
      break
    ans.append(a)
if ans == -1 : 
  print ans
else: 
  for a in ans: 
    print " ".join(map(str, a))