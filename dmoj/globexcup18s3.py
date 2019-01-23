import sys
input = sys.stdin.readline

def dammit(b, e):
  ans = 1
  while e:
    if e % 2:
      ans = (ans * b) % m
    b = (b * b) % m
    e /= 2
  return ans

n, m, k, v = map(int, input().split())

ans_xor = 1
ans_or = 1
ans_and = 1

cute = dammit(2, (n - 1)) % m
cuteness = (dammit(2, n) - 1) % m

for i in xrange(k): 
  ans_xor = (ans_xor * cute) % m 
  if v >> i&1: 
    ans_or = (ans_or * cuteness) % m    
  else: 
    ans_and = (ans_and * cuteness) % m    

print(ans_xor % m)
print(ans_or % m)
print(ans_and % m)
