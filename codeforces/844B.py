import sys
from math import factorial
input = sys.stdin.readline 

n, m = map(int, input().split())

cactus = ["cute" for _ in range(n)]
ans = -n * m

def ncr(n, r): 
  return factorial(n) / factorial(r) / factorial(n - r)

for i in range(n): 
  cactus[i] = list(map(int, input().split()))


for row in cactus: 
  l = len(row)
  s = sum(row)
  ans += 2 ** s - 1
  ans += 2 ** (l - s) - 1

for _ in range(m): 
  row = [cactus[i][_] for i in range(n)]

  l = len(row)
  s = sum(row)
  ans += 2 ** s - 1 
  ans += 2 ** (l - s) - 1

print ans 