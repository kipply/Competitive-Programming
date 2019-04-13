import sys, math, os
input = sys.stdin.readline

s = os.read(0, 10 ** 6 + 1)
ans = 0
x = 0

count = 0 
curr = 1
for i in xrange(len(s)): 
  if s[i] == 'b': 
    # print count
    ans += curr - 1 
    ans %= 1000000007
  else: 
    count += 1 
    curr *= 2
    curr %= 1000000007

print ans 