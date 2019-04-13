import sys
input = sys.stdin.readline 

a, d, m = map(int, input().split())
g, p, b = map(int, input().split())
ans = "YES"
if a <= g: 
  g -= a
else:
  ans = "NO" 
# print(g, p, b)
if d <= g + p: 
  t = min(d, g)
  g -= t 
  p -= d - t 
else: 
  ans = "NO" 
# print(g, p, b)
if m > sum ([g, b, p]): 
  ans = "NO" 
print ans