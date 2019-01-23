import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())

if k <= int(math.ceil(n / 2.0)): 
  print int(2 * (k - 1) + 1)
else: 
  print int(2 * (k - math.ceil(n / 2.0)))