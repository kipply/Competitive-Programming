import sys, math, os
input = sys.stdin.readline

n, a, b = map(int, input().split())
# ax + by = n
xs = [] 
for x in range(0, n / a + 1): 
  if (n - (a * x)) / float(b) == (n - (a * x)) / b: 
    xs.append(x)

ans = []
if len(xs): 
  x = xs[0] 
  y =  (n - (a * x)) / (b)
  curr = 0
  for i in range(x): 
    ans.append(curr + a) 
    ans.extend([j for j in range(curr + 1, curr + a)]) 
    curr += a 
  
  for i in range(y): 
    ans.append(curr + b) 
    ans.extend([j for j in range(curr + 1, curr + b)]) 
    curr += b
  ans = " ".join(map(str, ans))
  
else: 
  ans = -1 

print ans