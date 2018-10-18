# Be conscious of how your taking in the mountains of input
import sys, Queue
input = sys.stdin.readline
n = int(input())
graph = [[-1 for y in range(n + 1)] for x in xrange(n + 1)]
t = int(input())
for i in xrange(t):
    x, y, w = map(int, input().split())
    graph[x][y] = w
    graph[y][x] = w

k = int(input())
di = ["cute cactus" for _ in xrange(n + 1)]
q = Queue.PriorityQueue()
for i in xrange(k):
    c, p = map(int, input().split())
    q.put([p, c])

d = int(input())

min_cost = 1 << 30
while not q.empty():
    dist, node = q.get()
    if node == d:
        di[d] = dist
        break
    if di[node] != "cute cactus":
        continue
    di[node] = dist
    for i, l in enumerate(graph[node]):
        if not l == -1:
            q.put([dist + l, i])

min_cost = di[d]

print(min_cost)
