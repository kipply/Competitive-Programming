# 2D prefix sum
import sys
w = sys.stdin.readline().split(" ")
h = int(w[1])
n = int(w[2])
w = int(w[0])

f = [[0] * (w + 1)] * (h + 1)
for i in range(1, h + 1):
  f[i] = [0] + list(map(int, sys.stdin.readline().split(" ")))

for i in range(1, h + 1):
	for j in range(1, w + 1):
		f[i][j] += f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1];
ans = 0
if w == h and w * h == n + 1:
  i = h - 1
  wi = w
  for j in range(1, h - i + 2):
    for k in range(1, w - wi + 2):
      a = j - 1
      b = k - 1
      c = j + i - 1
      d = k + wi - 1
      if ans < f[c][d] - f[a][d] - f[c][b] + f[a][b]:
        ans = f[c][d] - f[a][d] - f[c][b] + f[a][b]
  i = h
  wi = w - 1
  for j in range(1, h - i + 2):
    for k in range(1, w - wi + 2):
      a = j - 1
      b = k - 1
      c = j + i - 1
      d = k + wi - 1
      if ans < f[c][d] - f[a][d] - f[c][b] + f[a][b]:
        ans = f[c][d] - f[a][d] - f[c][b] + f[a][b]
  print(ans)
else:
  for i in range(1, h + 1):
    wi = n // i
    if i * wi > n:
      continue
    for j in range(1, h - i + 2):
      for k in range(1, w - wi + 2):
        a = j - 1
        b = k - 1
        c = j + i - 1
        d = k + wi - 1
        if ans < f[c][d] - f[a][d] - f[c][b] + f[a][b]:
          ans = f[c][d] - f[a][d] - f[c][b] + f[a][b]
  print(ans)
