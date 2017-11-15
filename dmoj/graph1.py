import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [set() for _ in xrange(n + 1)]

for i in xrange(m):
    a, b = map(int, input().split())
    adj[b].add(a)
    adj[a].add(b)
x, y = map(int, input().split())
visited = [0 for _ in xrange(n + 1)]
q = []
q.append(x)
visited[x] = True
ans = 0
while len(q) > 0:
    curr = q.pop()
    for node in adj[curr]:
        if visited[node]:
            continue
        if node == y:
            ans += 1
        visited[node] = True
        q.append(node)
print ans
# I too, was very tilted by this problem.
