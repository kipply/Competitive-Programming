import sys
n = int(sys.stdin.readline())
flowers = sys.stdin.readline().split()
flowers = [int(i) for i in flowers]
flowers[:0] = [0]
m = int(sys.stdin.readline())
sub = 0
for i in range(m):
    a = sys.stdin.readline().split(" ")
    d = int(a[1])
    a = int(a[0])
    if d > flowers[a] and d > flowers[a + 1]:
        if flowers[a] > flowers[a + 1]:
            flowers[a + 1] = 0
        else:
            flowers[a] = 0
    elif d >= flowers[a] and d <= flowers[a + 1]:
        flowers[a] = 0
    elif d <= flowers[a] and d >= flowers[a + 1]:
        flowers[a + 1] = 0
    elif d < flowers[a] and d < flowers[a + 1]:
        sub += d
print(sum(flowers) - sub)
