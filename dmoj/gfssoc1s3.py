import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

friends = 1
g = []
px = [0 for x in range(t + 1)]
py = [0 for x in range(t + 1)]
for i in range(n):
    row = list(input().strip())
    g.append(row)
    for j in range(m):
        if row[j] == "H":
            px[friends], py[friends] = i, j
            g[i][j] = friends
            friends += 1
        if row[j] == "G":
            px[0], py[0] = i, j
            g[i][j] = 0

dr = [1, -1, 0, 0]
dc = dr[::-1]
dist = [[0 for y in range(t + 1)] for x in range(t + 1)]
for i in range(t + 1):
    q = []
    v = [[0 for x in range(m)] for y in range(n)]
    v[px[i]][py[i]] = 1
    q.append([px[i], py[i], 0])
    while q:
        person = q.pop(0)
        if isinstance(g[person[0]][person[1]], (int, long)):
          dist[i][g[person[0]][person[1]]] = person[2];
        for j in range(4):
            x2, y2 = person[0] + dr[j], person[1] + dc[j]
            if (x2 < 0 or y2 < 0 or x2 >= n or y2 >= m or v[x2][y2] or g[x2][y2] == 'X'):
                continue
            v[x2][y2] = 1
            q.append([x2, y2, person[2] + 1])
v = [0 for x in range(t + 1)]
v[0] = 1

def f(i, s, r):
    if r == 0:
        return s
    m = 1 << 30
    for x in range(t + 1):
        if not v[x]:
            v[x] = 1
            m = min(m, f(x, s + dist[i][x], r - 1))
            v[x] = 0
    return m
print(f(0, 0, t))
