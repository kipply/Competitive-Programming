import sys
input = sys.stdin.readline

f = int(input())
r = int(input())
c = int(input())
g = [[] for x in xrange(r)]
for i in xrange(r):
    g[i] = list(input())

ro = []
dr = [1, -1, 0, 0]
dc = dr[::-1]

def dfs(r, c):
    global count
    g[r][c] = "I"
    for i in range(4):
        r2 = r + dr[i]
        c2 = c + dc[i]
        try:
            if r2 > -1 and c2 > -1 and g[r2][c2] == ".":
                count += 1
                dfs(r2, c2)
        except:
            pass


for x in range(r):
    for j in range(c):
        if g[x][j] == ".":
            count = 1
            dfs(x, j)
            ro.append(count)

ro = sorted(ro)[::-1]
ans = 0
for x in ro:
    if x <= f:
        f -= x
        ans += 1
    else:
        break

if ans == 1:
    print(str(ans) + " room, " + str(f) + " square metre(s) left over")
else:
    print(str(ans) + " rooms, " + str(f) + " square metre(s) left over")
