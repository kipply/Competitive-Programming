import sys
input = sys.stdin.readline
sys.setrecursionlimit(1500000000)
n, m = map(int, input().split())

al = [{} for _ in range(n)]

destinations = [True for _ in range(n)]
entrances = [True for _ in range(n)]
visited = [False for _ in range(n)]
ans = 0
shortest =[1 << 30 for _ in range(n)]
def dfs(i, d):
  global ans
  visited[i] = True
  for j in al[i]:
    dfs(j, d + 1)
  if destinations[i]:
    ans += 1
    if d < shortest[i]:
      shortest[i] = d

for i in range(m):
  a, b = map(int, input().split())
  al[a][b] = 1
  destinations[a] = False
  entrances[b] = False
e = []
for i in range(n):
  if entrances[i]:
    dfs(i, 1)

print(ans % 1000000007)
for i in range(n):
  if destinations[i]:
    print(shortest[i], end=" ")
