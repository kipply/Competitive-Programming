n = int(input())
a = []
for i in range(n * 2):
  b = input()
  a.append(b)
psa = [0] * (n + 1)
for i in range(n):
  if a[i] == a[n+i]:
    psa[i + 1] = psa[i] + 1
  else:
    psa[i + 1] = psa[i]
print(psa[len(psa) - 1])
