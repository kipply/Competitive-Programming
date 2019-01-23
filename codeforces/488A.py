import sys
input = sys.stdin.readline

a = int(input()) + 1

ans = 1
while "8" not in str(a): 
  a += 1
  ans += 1

print ans