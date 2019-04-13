import sys
input = sys.stdin.readline 

n, k, a, b = map(int, input().split())
av = sorted(list(map(int, input().split())))

ans = 1 << 30

def solve(l, r, avengers): 
  if len(avengers): 
    if not r - l: 
      return b * len(avengers)
    mid = (l + r) / 2
    lo = 0
    hi = len(avengers)

    while hi > lo: 
      g = (hi + lo) / 2
      if avengers[g] <= mid: 
        lo = g + 1
      else: 
        hi = g
    res = solve(l, mid, avengers[:hi])
    res += solve(mid + 1, r, avengers[hi:])
    return min(res, len(avengers) * (r - l + 1) * b)
  else:
    return a

power = solve(1, 2 ** n, av)
print power