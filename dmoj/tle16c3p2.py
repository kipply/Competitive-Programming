import sys
input = sys.stdin.readline

p, n, v, r = map(int, input().split())

planets = []
for i in range(p): 
  planets.append(map(int, input().split()))

a = []
for i in range(n): 
  a.append(int(input()))

def get_y(x): 
  res = 0 
  for i in range(n): 
    res += a[i] * x ** (n-i)
  return res

exp_y = get_y(v)

ans = 0 
for x, y in planets: 
  if get_y(x) == y and x < v: 
    ans += 1 
    continue
  if ((exp_y - y)**2 + (v - x)**2) ** 0.5 <= r: 
    ans += 1 

print ans