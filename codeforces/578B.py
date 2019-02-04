import sys
input = sys.stdin.readline 

n, k, x = map(int, input().split())
l = list(map(int, input().split()))

p = [l[0]] + [0 for _ in range(n - 1)]
s = [0 for _ in range(n - 1)] + [l[-1]]
ans = 0
derp = x**k

for i in xrange(1, n): 
  p[i] = p[i - 1] | l[i]
  s[-i - 1] = s[-i] | l[-i -1]

# print s
# print p
for i in xrange(n): 
  if n == 1: 
    ans = l[i] * derp
  elif i == 0: 
    ans = max(ans, s[i + 1] | l[i] * derp)
  elif i == n - 1: 
    ans = max(ans, p[i - 1] | l[i] * derp)
  else: 
    ans = max(ans, p[i - 1] | s[i + 1] | l[i] * derp)

print ans