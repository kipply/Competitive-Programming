from sys import stdin
n, m = map(int, stdin.readline().split())
a, b, c = map(int, stdin.readline().split())
x = [0] + list(map(int, stdin.readline().split()))
x.sort()
software = [0] * (n + 2) # Extra array space == indices in range
engineering = [0] * (n + 2)
for i in range(1, n + 1):
  software[i] = (x[i] - 1) * b + software[i - 1]
for i in range(n, 0, -1):
  engineering[i] = engineering[i + 1] + (x[i] - 1) * a + c * (n - i)
mm = 696969969696996969669696420420420
for loo in range(n + 1):
  mm = min(mm, software[loo] + engineering[loo + 1])
print(mm)
