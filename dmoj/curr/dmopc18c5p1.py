import sys
input = sys.stdin.readline 

n, m, k = map(int, input().split())

n = ("0" * k + "{0:#b}".format(n)[2:])[::-1]
m = ("0" * k + "{0:#b}".format(m)[2:])[::-1]

# print n, m 

blue = 0 
purple = 0 

for i in range(k): 
  if int(n[i]) ^ int(m[i]): 
    blue += 1 
  else: 
    purple += 1 

print blue, purple
