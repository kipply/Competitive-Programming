import sys
ad = sys.stdin.readlines()
msg = ad[0].strip()

def edit_distance(buff):
    dp = [[0] * (len(buff)+1) for _ in xrange(2)]
    for j in xrange(len(buff)+1):
        dp[0][j] = j
    h = 1
    for i in xrange(1, len(msg)+1):
        dp[h][0] = i
        for j in xrange(1, len(buff)+1):
            if msg[i-1] == buff[j-1]:
                dp[h][j] = dp[h^1][j-1]
            else:
                dp[h][j] = min(dp[h^1][j-1], min(dp[h^1][j], dp[h][j-1])) + 1
        h ^= 1
    return dp[len(msg)&1][len(buff)]

N = int(ad[1])
ret = 105 # MAXC
for i in xrange(N):
    K = ad[i+2].split()
    K[0] = int(K[0])
    res = 0
    for j in xrange(1, K[0]+1):
        res += edit_distance(K[j])
    ret = min(1.0 * res / K[0], ret)
print '%.6f' % ret
