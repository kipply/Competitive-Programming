import sys
input = sys.stdin.readline 

n = int(input())
h = list(map(int, input().split()))
h[0] = h[-1] = 1
ans = 0 

for i in range(1, n): 
  h[i] = min(h[i], h[i - 1] + 1)

for i in range(n - 2, -1, -1): 
  h[i] = min(h[i], h[i + 1] + 1)

print max(h)