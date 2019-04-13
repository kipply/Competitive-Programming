import sys
input = sys.stdin.readline 

n, t = map(int, input().split())
a = list(map(int, input().split()))

dp = [0 for _ in range(301)]

for i in a * min(t, 2 * n): 
  dp[i] = max(dp[:i + 1]) + 1

max_n = max(dp)

count = [0 for _ in range(301)]
for x in a: 
  count[x] += 1

print(max_n + max((t - n * 2) * max(count), 0))