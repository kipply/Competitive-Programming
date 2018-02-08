import sys
input = sys.stdin.readline

w = []
h = []
for i in range(int(input())):
    a, b = map(int, input().split())
    w.append(a)
    h.append(b)

print (max(w) - min(w)) * (max(h) - min(h))
