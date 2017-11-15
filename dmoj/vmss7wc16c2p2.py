g = raw_input()
l = len(g)
q = int(input())
u = 0
psa = [0] * (l + 1)
for i in range(q):
  a = raw_input().split(" ")
  i = int(a[0])
  j = int(a[1]) + 1
  if j > u:
    for k in range(u, j):
      psa[k+1] = psa[k]
      if g[k] == 'G':
        psa[k+1] += 1
    u = j
  print(psa[j] - psa[i])
