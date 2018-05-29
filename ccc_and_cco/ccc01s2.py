import sys
import math
input = sys.stdin.readline
n = int(input())
m = int(input())
s = int(math.ceil((m - n) ** 0.5)) + 2
spiral = [['' for _ in range(s)] for _ in range(s)]
r = s / 2
c = s / 2
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
d = -1
for x in range(n, m + 1):
    for y in range(s):
        r += dr[d]
        c += dc[d]
        if spiral[r][c] == '':
            spiral[r][c] = str(x)
            break
    if n == m:
        break
    nd = (d + 1) % 4
    if spiral[r + dr[nd]][c + dc[nd]] == '':
        d = nd
for i in range(len(spiral)):
    for j in range(len(spiral[i])):
        if spiral[i][j] == "":
            spiral[i][j] = "  "
for row in spiral:
    print " ".join(row)
