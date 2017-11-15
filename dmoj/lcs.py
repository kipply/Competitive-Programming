def lcs():
    m = len(x)
    n = len(y)

    dp = [[None] * (n + 1) for i in xrange(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
    return dp[m][n]

n, m = map(int, raw_input().split())
x = list(map(int, raw_input().split()))
y = list(map(int, raw_input().split()))

print lcs()
