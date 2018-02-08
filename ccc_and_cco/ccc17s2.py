import sys
input = sys.stdin.readline

n = int(input())
t = sorted(list(map(int, input().split())))
if n % 2:
    lo = t[:n / 2 + 1][::-1]
    hi = t[n / 2 + 1:]
else:
    lo = t[:n / 2][::-1]
    hi = t[n / 2:]
f = True
ans = []
while len(lo) or len(hi):
    if f:
        ans.append(lo.pop(0))
    else:
        ans.append(hi.pop(0))
    f = not f
print " ".join(list(map(str, ans)))
