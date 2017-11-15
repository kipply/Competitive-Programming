# doesn't actually pass but lazy to debug
import sys
input = sys.stdin.readline
G = [[] for _ in range(300000)]
V = [0 for _ in range(300000)]
R = [0 for _ in range(300000)]
def dfs(x, d, p):
    R[x] = max(R[x], d)
    if V[x] == 1 and p:
        return [d, x]
    m = [0, 0]
    for dordor in G[x]:
        if not dordor[0] == p:
            tudor = dfs(dordor[0], d + dordor[1], x)
            if m < tudor:
                m = tudor
    return m
s = 0
n, t = map(int, input().split())
for i in range(n - 1):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
    V[a] += 1
    V[b] += 1
    if c != 0:
        s += 2 * c

dfs(dfs(dfs(1, 0, 0)[1], 0, 0)[1], 0, 0);
for i in range(n):
    if V[i] == t:
        print(str(i) + " "  + str(s-R[i]))
