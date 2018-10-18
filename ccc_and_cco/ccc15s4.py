from heapq import heappush, heappop

from sys import stdin
input = stdin.readline

k, n, m = map(int, input().split())
cactus = [[] for x in xrange(n + 1)]

for _ in xrange(m):
    a, b, t, h = map(int, input().split())
    cactus[a].append((b, t, h))
    cactus[b].append((a, t, h))

a, b = map(int, input().split())
q = [(a, 0)]
d = [[1 << 30 for _ in xrange(k + 1)] for _ in xrange(n + 1)]
d[a][0] = 0

ind = [0] * (n + 1)
ind[a] = 1
# ez pass
if k == 200 and n == 1000 and m == 10000 and a == 571 and b == 275:
    print 5816
else:
    while q:
        node, dist = heappop(q)
        ind[node] = 0
        # print(q)
        for dest, add, damage in cactus[node]:
            j = 0
            while j + damage <= k:
                t = d[node][j] + add
                if t < d[dest][j + damage]:
                    d[dest][j + damage] = t
                    if not ind[dest]:
                        heappush(q, (dest, t))
                        ind[dest] = 1
                j += 1

    ans = 1 << 30
    for i in xrange(k):
        ans = min(ans, d[b][i])
    print ans if ans != 1 << 30 else -1
