import sys
input = sys.stdin.readline 

n, k, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
psa = [0 for _ in range(n + 1)]
for i in range(1, n + 1): 
  psa[i] = psa[i - 1] + a[i - 1]

ans = -1
for i in xrange(min(n, m + 1)): 
  attempt = ((psa[-1] - psa[i]) + min(k * (n - i), m - i)) / float(n - i)
  ans = max(ans, attempt)

print ans