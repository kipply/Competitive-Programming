import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = (n * (n - 1)) / 2
counts = [0 for _ in range(m + 1)]
for x in a: 
  counts[x] += 1 

for count in counts: 
  if count > 1: 
    ans -= (count * (count - 1)) / 2

print ans