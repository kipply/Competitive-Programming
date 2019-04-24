import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
c = list(map(int, input().split()))

s = 0
cc = 0
ans = 0
  
for i in range(n): 
  if ((s + c[i]) < m): 
    s += c[i] 
    cc += 1

  elif(s): 
    s = s - c[i - cc] + c[i] 
  ans = max(cc, ans) 
print ans