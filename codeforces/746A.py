import sys
input = sys.stdin.readline 

n, m, z = map(int, input().split())

minute = 1 
kills = 0
while minute <= z: 
  if not minute % n and not minute % m: 
    kills += 1
  minute += 1
print kills