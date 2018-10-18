import sys
input = sys.stdin.readline

d = {}
ans = 0
for i in range(int(input())):
    name = input().strip()
    try:
        d[name] += 1
    except KeyError:
        d[name] = 1
    if d[name] - 1 > sum(d.values()) - d[name]:
        ans += 1
print ans
