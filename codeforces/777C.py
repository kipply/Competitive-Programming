import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())

table = [list(map(int, input().split())) for _ in xrange(n)]
pre = [[0 for _ in xrange(m)] for _ in xrange(n - 1)]
pre.append([n - 1 for _ in xrange(m)])

maxes = [0 for i in range(n)]

for i in xrange(n - 2, -1, -1): 
  for j in xrange(m): 
    if table[i][j] <= table[i + 1][j]: 
      pre[i][j] = pre[i + 1][j]
    else: 
      pre[i][j] = i
    maxes[i] = max(maxes[i], pre[i][j])

# for row in pre: print row
k = int(input())
for _ in xrange(k): 
  ans = "No" 
  t, b = map(int, input().split())
  if maxes[t - 1] >= b - 1: 
    ans = "Yes"

  print ans