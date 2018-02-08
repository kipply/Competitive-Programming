import sys
input = sys.stdin.readline

n = int(input())

m = []
for i in range(n):
    t = sorted(list(map(int, input().split())))
    m.append(t[n / 2])
# print m
m = sorted(m)
print m[n / 2]