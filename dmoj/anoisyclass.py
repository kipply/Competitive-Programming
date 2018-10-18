import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cactus = [set() for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    cactus[a].add(b)

ans = "Y"

def dfs(n):
    global ans
    global v
    if vv[n]:
        return
    if v[n]:
        ans = "N"
        return
    v[n] = 1

    for x in cactus[n]:
        dfs(x)
    v[n] = 0
    vv[n] = 1
v = [0 for x in range(n + 1)]
vv = [0 for x in range(n + 1)]
for i in range(1, n + 1):
    if not vv[i]:
        dfs(i)
print ans
