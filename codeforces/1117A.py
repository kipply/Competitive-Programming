import sys
input = sys.stdin.readline 

n = int(input())
a = list(map(int, input().split()))
m = max(a) 

cccccccombo = 0
curr = 0 
for i in range(n): 
  if a[i] == m: 
    curr += 1 
  else: 
    if curr > cccccccombo: 
      cccccccombo = curr
    curr = 0 
if curr > cccccccombo: 
  cccccccombo = curr

print cccccccombo