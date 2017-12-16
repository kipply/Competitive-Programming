ans = 100
ansans = 100
for i in range(int(input())):
  a, d = map(int, input().split())
  if a > d:
    ansans -= a
  if d > a:
    ans -= d
print(ans)
print(ansans)
