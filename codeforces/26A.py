import sys
input = sys.stdin.readline 

n = int(input())

ans = 0 

for x in range(3, n + 1):
  i = 2
  factors = set()
  while i * i <= x:
    if x % i:
      i += 1
    else:
      x /= i
      factors.add(i)
  if x > 1: 
    factors.add(x)
  if len(factors) == 2: 
    ans += 1

print ans