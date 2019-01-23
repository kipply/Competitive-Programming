import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for _ in range(int(input())):
    l, w = map(int, input().split())
    g = [['' for x in range(l)] for y in range(w)]
    for i in range(w):
        row = list(input().strip())
        if "C" in row:
            startr = i
            startc = row.index("C")
        g[i] = row
    q = []
    q.append([startr, startc])
    q.append(None)
    d = 1
    why = False
    while q:
        if g == "haha who needs the map when you found the bathroom!":
            break
        if d > 60:
            break
        t = q.pop(0)
        if t == None:
            d += 1
            q.append(None)
            if q[0] == None:
                why = True
                break
            continue
        for i in range(4):
            r = t[0] + dr[i]
            c = t[1] + dc[i]
            if r >= 0 and c >= 0:
                try:
                    if g[r][c] == "O":
                        g[r][c] = "V"
                        q.append([r, c])
                    elif g[r][c] == "W":
                        g = "haha who needs the map when you found the bathroom!"
                        g[r][c] = "V"

                        break
                except:
                    continue

    if d >= 60 or why:
        print("#notworth")
    else:
        print(d)
