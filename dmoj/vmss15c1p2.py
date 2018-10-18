import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [['' for x in range(c)] for y in range(r)]
for i in range(r):
    row = list(input().strip())
    grid[i] = row

ans = 0
dr = [1, -1, 0, 0]
dc = dr[::-1]
def dfs(r, c):
    global ans
    grid[r][c] = "*"
    for x in range(4):
        try:
            if grid[r + dr[x]][dc[x] + c] == "." and r + dr[x] > -1 and dc[x] + c > -1:
                dfs(r + dr[x], dc[x] + c)
        except:
            pass


for i in range(r):
    for j in range(c):
        if grid[i][j] == '.':
            dfs(i, j)
            ans += 1
print(ans)
