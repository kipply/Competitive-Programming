import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s, t = map(int, input().split())

cactus = [[] for x in range(n + 1)]
points = set()
for i in range(m):
    a, b, c, d = map(int, input().split())
    cactus[a].append((b, c, d))
    points.add(c)
    points.add(d + 1)

ans = 0
points = sorted(list(points))
for x in range(len(points)):
    i = points[x]
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
    try:
        diff = points[x + 1] - i
    except:
        diff = k - i
    ans += diff if f else 0

print ans