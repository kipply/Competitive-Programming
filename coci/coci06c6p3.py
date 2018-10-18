import sys
input = sys.stdin.readline
n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

xmoves = [-1, -1, -1, 0, 0, 1, 1, 1]
ymoves = [-1, 0, 1, -1, 1, -1, 0, 1]
def f(x, y, dx, dy, i, c):
    if x < 0 or x >= n or y < 0 or y >= n or not grid[x][y] == c:
        return False
    if i == 0:
        return True
    return f(x + dx, y + dy, dx, dy, i - 1, c)
dordor = True
for i in range(n):
    for j in range(n):
        if grid[i][j] != ".":
            for k in range(4):
                if f(i + xmoves[k], j + ymoves[k], xmoves[k], ymoves[k], 1, grid[i][j]):
                    print(grid[i][j])
                    dordor = False
                    sys.exit()

if dordor: print('ongoing')
