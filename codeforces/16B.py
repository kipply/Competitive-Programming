import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
matches = sorted([map(int, input().split()) for _ in range(m)], key=lambda x:x[1])[::-1]
ans = 0 
for match in matches: 
  if not n: break
  ans += min(n, match[0]) * match[1]
  n -= min(n, match[0])

print ans