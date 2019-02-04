import sys
input = sys.stdin.readline 

n, m, c_0, d_0 = map(int, input().split())

 # dp[grams_of_dough][1..j stuffings]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# grams left, grams required, dough required, sell price
stuffing = [(0, 1, 0, 0)] + [map(int, input().split()) for _ in range(m)]

for i in range(0, n + 1): 
  for j in range(1, m + 1): 
    # attempt to make k of j-stuffed thingies
    for k in range(stuffing[j][0] / stuffing[j][1] + 1):
      if i - stuffing[j][2] * k > -1: 
        dp[i][j] = max(dp[i - stuffing[j][2] * k][j - 1] + stuffing[j][3] * k, dp[i][j])


ans = 0 
# for row in dp: print row
for k in range(n + 1): 
  ans = max(ans, dp[k][m] + ((n - k) / c_0) * d_0)

print ans