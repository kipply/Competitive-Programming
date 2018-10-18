import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
cactus = [[] for x in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    cactus[a].append(b)

d = [[0 for x in range(n + 1)] for x in range(n + 1)]
for i in range(1, n + 1):
    q = [i, None]
    v = [0 for x in range(n + 1)]
    depth = 0
    while q:
        node = q.pop(0)
        if node == None:
            q.append(None)
            if q[0] == None:
                break
            depth += 1
            continue
        for dest in cactus[node]:
            if not d[i][dest]:
                d[i][dest] = depth + 1
                q.append(dest)

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    print((d[a][b] * t) if d[a][b] else "Not enough hallways!")
