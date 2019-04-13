import sys, math, os
input = sys.stdin.readline

n = int(input())

factors = []
if n == 1: 
  factors.append(1)
while not n % 2: 
  n /= 2 
  factors.append(2)
for x in range(3, int(n ** 0.5) + 1, 2): 
  while not n % x: 
    factors.append(x) 
    n /= x 
if n > 2: 
  factors.append(n)

ans = 0 
m = (0, 0)
counts = {}
for f in set(factors): 
  counts[f] = factors.count(f)
  if counts[f] > m[0]: 
    m = (counts[f], f)
ans += math.ceil(math.log(m[0], 2))

for f in set(factors): 
  if ans != math.log(counts[f], 2): 
    ans += 1
    break


print reduce(lambda x, y: x * y, list(set(factors))), int(ans)