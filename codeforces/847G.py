import sys, math
input = sys.stdin.readline

n = int(input())

rooms = [0 for _ in range(7)] 
for i in range(n): 
  cute = list(map(int, list(input().strip())))
  for j in range(7): 
    rooms[j] += cute[j]

print max(rooms)