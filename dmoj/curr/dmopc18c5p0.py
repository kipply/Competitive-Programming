import sys
input = sys.stdin.readline 

s = input().strip()
base = list(map(float, input().split()))
top = list(map(float, input().split()))

if s == "Multiply": 
  for i in range(3): 
    base[i] *= top[i]


if s == "Screen": 
  for i in range(3): 
    base[i] = 1 - (1 - base[i]) * (1 - top[i])


if s == "Overlay": 
  for i in range(3): 
    if base[i] <= 0.5: 
      base[i] *= 2 * top[i]
    else: 
      base[i] = 1 - 2*(1 - base[i]) * (1 - top[i])

print " ".join(map(str, base))