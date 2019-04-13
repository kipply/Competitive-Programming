import sys, math
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

doubles = 0 
while len(a) > 1: 
  if a[0] == a[1]: 
    doubles += 1 
    a = a[2:]
  else: 
    a = a[1:] 
print doubles / 2