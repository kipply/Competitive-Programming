import sys
input = sys.stdin.readline 

n, k, a, b = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = 1 << 30

lo = 0
hi = 2**n - 1

while lo < hi:
  curr = (lo + hi) // 2
