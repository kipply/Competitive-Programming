import sys, math, os
input = sys.stdin.readline

n, k, m = map(int, input().split())

a = list(map(int, input().split()))

cactus = {} 
for x in a: 
  if x % m in cactus: 
    cactus[x % m].append(x)
  else: 
    cactus[x % m] = [x]


f = 0
for bloop in cactus: 
  if len(cactus[bloop]) >= k: 
    f = 1 
    print "Yes"
    print " ".join(map(str, cactus[bloop][:k]))
    break
if not f: 
  print "No"