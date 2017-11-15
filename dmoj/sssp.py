import Queue
import sys
input = sys.stdin.readline
q = Queue.PriorityQueue()
n, m = map(int, input().split())

d = [-1 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for l in range(m):
    x, y, z = map(int, input().split())
    adj[x].append([y, z])
    adj[y].append([x, z])

q.put([0, 1])
while not q.empty():
    dist, node = q.get()
    if d[node] != -1: # if it's been visited?
        continue
    d[node] = dist
    for l in adj[node]:
        q.put([dist + l[1], l[0]])

for l in range(1, n + 1):
    print(d[l])
