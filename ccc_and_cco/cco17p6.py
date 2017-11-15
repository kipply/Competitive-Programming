# down, right, up, left will cause three pieces to cycle like a PLL Algorithm!
# Please don't try to read this code :(
from sys import stdin
def YOUDIDSOMETHING(xxx, k):
    xxx += 1
    if k < 0:
        ans.append("1 " + str(xxx) + " " + str(m + k))
    else:
        ans.append("1 " + str(xxx) + " " + str(k))
def YOUDIDSOMETHINGELSE(yyy, k):
    yyy += 1
    if k < 0:
        ans.append("2 " + str(yyy) + " " + str(n + k))
    else:
        ans.append("2 " + str(yyy) + " " + str(k))
def rotate(x, y, yy, xx):
    x %= n
    xx %= n
    y %= m
    yy %= m
    YOUDIDSOMETHING(x, y - yy)
    YOUDIDSOMETHINGELSE(y, x - xx)
    YOUDIDSOMETHING(x, yy - y)
    YOUDIDSOMETHINGELSE(y, xx - x)
    tmp = grid[x][y]
    grid[x][y] = grid[x][yy]
    grid[x][yy] = grid[xx][y]
    grid[xx][y] = tmp
def reverseRotate(x, y, yy, xx):
    x %= n;
    y %= m;
    yy %= m;
    xx %= n;
    YOUDIDSOMETHINGELSE(y, x - xx)
    YOUDIDSOMETHING(x, y - yy)
    YOUDIDSOMETHINGELSE(y, xx - x)
    YOUDIDSOMETHING(x, yy - y)
    t = grid[x][y]
    grid[x][y] = grid[xx][y]
    grid[xx][y] = grid[x][yy]
    grid[x][yy] = t
def rotateRotate(y):
    reverseRotate(n - 1, y, y - 1, n - 2)
    rotate(n - 1, y, y + 1, n - 2)
def reverseRotateRotate(y):
    reverseRotate(n - 1, y, y + 1, n - 2)
    rotate(n - 1, y, y - 1, n - 2)
n, m = map(int, stdin.readline().split())
ans= []
grid = [0] * n
for i in range(n):
    grid[i] = list(map(int, stdin.readline().split()))
def innerK():
    for k in range(j + 1, m):
        if grid[i][k] == t:
            reverseRotate(i, k, j, i + 1)
            return
def innerKK():
    for k in range(i + 1, n):
        for l in range(m):
            if grid[k][l] == t:
                if l == j:
                    rotate(k, j, (l + 1) % m, i)
                else:
                    reverseRotate(k, j, l, i)
                return
for i in range(n - 1 ):
    for j in range(m):
        t = i * m + j
        if grid[i][j] == t:
            continue
        innerK()
        innerKK()
def innerInner():
    for j in range(i + 1, m):
        if grid[n - 1][j] == t:
            if j == m - 1:
                rotateRotate(m - 2)
                j = j - 1
            for k in range(j, i, -1):
                rotateRotate(k)
            return
for i in range(m - 2):
    t = (n - 1) * m + i
    if grid[n - 1][i] == t:
        continue
    innerInner()
if grid[n - 1][m - 2] == (n - 1) * m + (m - 1):
    i = m - 2
    while i != 0:
        reverseRotateRotate((i - 1) % m)
        i = (i - 2) % m
    YOUDIDSOMETHING(n - 1, -1)
print(len(ans))
for i in ans:
    print(i)
