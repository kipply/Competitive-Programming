import sys
input = sys.stdin.readline

cute = input().strip() 

cutes = cute.count("a")
uncutes = len(cute) - cutes

if (cutes == 0): 
  print(0)
else: 
  print(len(cute) - max(uncutes - cutes + 1, 0))