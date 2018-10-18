import sys

f = open('qr16b.in', 'r').readlines()[::-1]
out = open('qr16b.out', 'w')
input = f.pop

# input = sys.stdin.readline

t = int(input())
for _ in range(t):
    bi = input().strip()
    ans = 0
    while "-" in bi:
        new = list(bi[:bi.rfind("-")])
        for i in range(len(new)):
            new[i] = "-" if new[i] == "+" else "+"
        bi = "".join(new)
        ans += 1
    out.write("Case #%d: %d\n" % (_ + 1, ans))
