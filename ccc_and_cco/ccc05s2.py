import sys
input = sys.stdin.readline
lx = 0
ly = 0
c, r = map(int, input().split())
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    lx += x
    ly += y
    if lx > c:
        lx = c
    if lx < 0:
        lx = 0
    if ly > r:
        ly = r
    if ly < 0:
        ly = 0
    print(str(lx) + " " + str(ly))