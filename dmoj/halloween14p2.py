import sys

n = sys.stdin.readline().split()
w = int(n[1])
n = int(n[0])

CUTENESS = [0] * (n + 1)
FATNESS = [0] * (n + 1)
MOSTCUTE = [0] * (n + 1)
CATGIRLS = 1

for i in range(n):
    t = sys.stdin.readline().rstrip().split()
    if t[0] == 'A':
        FATNESS[CATGIRLS] = int(t[1]) + FATNESS[CATGIRLS - 1]
        CUTENESS[CATGIRLS] = int(t[2]) + CUTENESS[CATGIRLS - 1]
        l = 0
        h = CATGIRLS
        while l <= h:
            m = l + (h - l) / 2
            if FATNESS[CATGIRLS] - FATNESS[m] <= w:
                h = m - 1
            else:
                l = m + 1
        MOSTCUTE[CATGIRLS] = max(MOSTCUTE[CATGIRLS - 1], CUTENESS[CATGIRLS] - CUTENESS[l])
        print MOSTCUTE[CATGIRLS]
        CATGIRLS += 1
    else:
        CATGIRLS -= 1
