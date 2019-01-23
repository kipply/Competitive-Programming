import sys
from math import sqrt
input = sys.stdin.readline

r, x, y = map(int, input().split())

stars = [] 
for i in range(3): 
	stars.append(list(map(int, input().split())))

stars.sort(key=lambda x: x[2])

# print(stars) 

sx = stars[0][0]
sy = stars[0][1] 

if ((sx - x)**2.0 + (sy - y)**2.0)**0.5 >= r: 
	print("Time to move my telescope!")
else: 
	print("What a beauty!")
