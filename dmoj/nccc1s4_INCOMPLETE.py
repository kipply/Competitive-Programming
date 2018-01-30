import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s, t = map(int, input().split())

cactus = [[] for x in range(n + 1)]

for i in range(m):
    a, b, c, d = map(int, input().split())
    cactus[a].append((b, c, d))

ans = 0
for i in range(1, k + 1):
    visited = [0] * (n + 1)
    f = 0
    q = [s]
    while len(q) > 0:
        curr = q.pop()
        for node, c, d in cactus[curr]:
            if visited[node]:
                continue
            if i < c or i > d:
                continue
            if node == t:
                f += 1
            visited[node] = True
            q.append(node)
    ans += 1 if f else 0

print ans