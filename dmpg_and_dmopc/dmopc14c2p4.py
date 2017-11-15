import sys

n = int(input())
t = [0] * n
for i in range(n):
  t[i] = int(sys.stdin.readline())
psa = [0] * (n + 1)
for i in range(0, len(t)):
  psa[i + 1] = psa[i] + t[i]
q = int(input())
for i in range(q):
  a = sys.stdin.readline().split(" ")
  b = int(a[1]) + 1
  a = int(a[0])
  print(psa[b] - psa[a])
