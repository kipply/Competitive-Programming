import sys, math, os
input = sys.stdin.readline

f = "YES"

for _ in range(8): 
  l = input().strip()
  if l != "WBWBWBWB" and l != "BWBWBWBW": 
    f = "NO" 
    break
print f