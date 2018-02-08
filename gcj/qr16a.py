import sys

f = open('qr16a.in', 'r').readlines()[::-1]
out = open('qr16a.out', 'w')
input = f.pop

# input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if not n:
        out.write("Case #%d: INSOMNIA\n" % (_ + 1))
        continue
    seen = set()
    val = n

    while len(seen) < 10:
        for l in str(val):
            seen.add(l)
        val += n
    out.write("Case #%d: %d\n" % (_ + 1, val - n))