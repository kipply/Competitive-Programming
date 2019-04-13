import sys, math, os
input = sys.stdin.readline

n = int(input())
good = list(map(int, input().split()))

dp = [0 for _ in range(max(good) + 1)]


for x in good: 
  divisors = set()
  for d in range(2, int(x ** 0.5) + 1): 
    if not x % d: 
      divisors.add(d)
      divisors.add(x/d)
  divisors.add(x)
  # print divisors
  if divisors: 
    dp[x] = max([dp[d] for d in divisors]) + 1
    for d in divisors: 
      dp[d] = dp[x]

if len(good) == 1: 
  print 1
else: 
  print max(dp)