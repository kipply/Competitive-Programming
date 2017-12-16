import sys
input = sys.stdin.readline

n, m = map(int, input().split())
val = list(map(int, input().split()))
bit = [[0] * (100005), [0] * (100005)]

def add(i, x, d):
    while(i <= 100000):
        bit[d][i] = bit[d][i] + x
        i += i &- i

def acc(h, d):
    ret = 0
    while h > 0:
        ret += bit[d][h]
        h -= h & -h
    return ret


def update(i, x, d):
    add(i, x - val[i], d)

def range_sum(l, h):
    return acc(h, 0) - acc(l - 1, 0)

for l in range(n): # build
    add(l + 1, val[l], 0)
    add(val[l], 1, 1)

for l in range(m):
    d = sys.stdin.readline().split()
    t = d[0]
    x = int(d[1])
    if (len(d) > 2):
        y = int(d[2])
    if (t == 'Q'):
        print(acc(x, 1))
    if (t == 'S'):
        print(range_sum(x, y))
    if (t == 'C'):
        add(x, -val[x - 1], 0)
        add(x, y, 0)
        add(val[x - 1], -1, 1)
        add(y, 1, 1)
        val[x - 1] = y
