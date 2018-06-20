import sys
input = sys.stdin.readline

n, c = map(int, input().split())
cactus = [0 for _ in range(n + 1)]
for i in range(c):
    a, b = map(int, input().split())
    cactus[a] += 1
    cactus[b] += 1

hi = 0
for z in range(n + 1):
    if cactus[z] >= hi:
        hi = cactus[z]
        ans = z

print ans
