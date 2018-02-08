import sys
input = sys.stdin.readline

n, m = map(int, input().split())

g = []
for i in range(n): g.append(list(input().strip()))

for _ in range(100):
    for r in range(n):
        for c in range(m):
            if g[r][c] == "o" and g[min(r + 1, n - 1)][c] == ".":
                g[r][c] = "."
                g[r + 1][c] = "o"

for row in g: print "".join(row)