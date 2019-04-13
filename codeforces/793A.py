import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
low = a[0]
ans = 0 
for x in a[1:]: 
  if (x - low) % k: 
    ans = -1 
    break
  else: 
    ans += (x - low) / k

print ans