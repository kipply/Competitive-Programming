import sys
import math
input = sys.stdin.readline
t = int(input())
for oops in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(str(n) + ("\n" * int(oops != t - 1)))
        continue
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
        nd = (d + 1) % 4
        if spiral[r + dr[nd]][c + dc[nd]] == '':
            d = nd

    # for row in spiral: print row

    while True:
        if all(x == '' for x in spiral[0]): spiral = spiral[1:]
        elif all(x == '' for x in spiral[-1]): spiral = spiral[:-1]
        elif all(x == '' for x in [_[0] for _ in spiral]):
            for i in range(len(spiral)): spiral[i] = spiral[i][1:]
        else:
            break
    #
    # for row in spiral: print row
    for i in range(len(spiral)):
        for j in range(len(spiral[i])):
            reeeeeeee = ""
            for reee in range(len(spiral)):
                try:
                    if int(spiral[reee][j]) >= 10:
                        reeeeeeee = " "
                except: pass
            if spiral[i][j] == "":
                    spiral[i][j] = " "
            if len(spiral[i][j]) == 1 and m >= 10: spiral[i][j] = reeeeeeee + spiral[i][j]

    for row in spiral:
        reeee = ""
        m = max(len(" ".join(spiral[-1]).rstrip()), len(" ".join(spiral[0]).rstrip()))
        if len(" ".join(row).rstrip()) < m:
            reeee = " " * (m - len(" ".join(row).rstrip()))
        print " ".join(row).rstrip() + reeee
    if not oops == t - 1: print"\n"
