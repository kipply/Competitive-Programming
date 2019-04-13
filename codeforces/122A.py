import sys, math
input = sys.stdin.readline

n = int(input())
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
ans = "NO"
for x in lucky_numbers: 
  if not n % x: 
    ans = "YES" 
    break
print ans