import sys 
input = sys.stdin.readline

t = int(input())
m = 2000000

p = [1 for l in range(2000000 + 1)]
def sieve(n):
  for i in range(2, n + 1):
    if p[i]:
      for j in range(2 * i, n + 1, i): 
        p[j] = 0

sieve(2000000)

for i in range(t): 
  n = int(input())
  for i in range(n, 2, -1): 
    if p[i] and p[2 * n - i]: 
      print i, (2 * n) - i
      break