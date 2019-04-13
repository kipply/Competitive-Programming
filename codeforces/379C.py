import sys, math, os
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
s = sorted(xrange(len(a)), key=lambda x:a[x])

counts = {} 
counts.setdefault(0)

ne = a[s[0]] - 1

for cute in xrange(n): 
  i = s[cute]

  if ne >= a[i]: 
    a[i] = ne
    ne += 1
  elif ne < a[i]: 
    ne = a[i] + 1

print " " .join(map(str, a))