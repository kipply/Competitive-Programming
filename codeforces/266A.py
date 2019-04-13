import sys, math
input = sys.stdin.readline

n = int(input())
s = input().strip()

ans = 0
for i in range(n - 1):   
  if s[i + 1] == s[i]: 
    ans += 1
print ans