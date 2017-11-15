# Not a good solution, but test cases are weak.
from sys import stdin
l, r, w = map(int, stdin.readline().split())
ll = list(map(int, stdin.readline().split()))
rr = list(map(int, stdin.readline().split()))
ll = sorted(ll)[::-1]
rr = sorted(rr)[::-1]
if sum(ll) > sum(rr):
  f = True
else:
  f = False
a = 0
sl = sum(ll)
sr = sum(rr)
while sum(ll) or sum(rr):
  if f:
    t = 0
    for boop in range(len(ll)):
      if t > sl - sr + w:
        break
      if t + ll[boop] > sl - sr + w:
        continue
      t += ll[boop]
      ll[boop] = 0
    a += 1
    f = False
    sl = sum(ll)
    sr = sum(rr)
  else:
    t = 0
    for boop in range(len(rr)):
      if t > sr - sl + w:
        break
      if t + rr[boop] > sr - sl + w:
        continue
      t += rr[boop]
      rr[boop] = 0
    a += 1
    f = True

    sl = sum(ll)
    sr = sum(rr)
print(a)
