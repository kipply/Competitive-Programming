import sys
input = sys.stdin.readline

cute = [] 
while 1: 
  city = input().split()
  temp = int(city[1])
  city = city[0]
  cute.append((city, temp))
  if city == "Waterloo": 
    break

cute.sort(key=lambda x: -x[1])

print(cute[-1][0])