import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
cactus = [[] for _ in range(n + 1)]

for i in range(n - 1): 
  a, b = map(int, input().split())
  cactus[a].append(b)
  cactus[b].append(a)

dp = [[1] + [0 for _ in xrange(k)] for _ in xrange(n + 1)] 
v = [0 for _ in range(n + 1)]
q = [1]
ans = 0

for node in q:
  for node_ in cactus[node]: 
    cactus[node_].remove(node)
  q.extend(cactus[node])
q = q[::-1]

while q: 
  node = q.pop(0)
  if v[node]: continue
  v[node] = True
  for next_node in cactus[node]:
    for i in xrange(k): 
      ans += dp[node][i] * dp[next_node][k - i - 1]
    for i in xrange(k): 
      dp[node][i + 1] += dp[next_node][i]

print ans