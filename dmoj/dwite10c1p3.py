import sys, math
input = sys.stdin.readline

def highpow(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return (x >> 1) + 1

def solve(m, n):
    global ans
    if m == 0 or n == 0:
        return
    z = highpow(min(m, n))
    ans += 1
    solve(min(n, m) - z, z)
    solve(min(n, m), max(n, m) - z)

for _ in range(5):
    w, h = map(int, input().split())
    ans = 0
    solve(w, h)
    print ans
