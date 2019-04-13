import sys, math
input = sys.stdin.readline

n, s = map(int, input().split())
one_million = 10 ** 6 
pi = 3.14159265358979323
cities = [] 
for _ in xrange(n): 
  x, y, k = map(int, input().split())
  d = (y * y + x * x) ** 0.5
  cities.append((d, k))

cities.sort()
# print cities
ans = -1 
for i, (distance, population) in enumerate(cities): 
  # print s
  s += population 
  if s >= one_million: 
    ans = distance
    break

print ans