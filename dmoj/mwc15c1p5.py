a = input().lower()
aa = 0
b = input().lower()
bb = 0
for l in range(len(a)):
  aa += pow(ord(a[l]) - ord('a') + 1, (l) % 4 + 1, 10)
for l in range(len(b)):
  bb += pow(ord(b[l]) - ord('a') + 1, (l) % 4 + 1, 10)
aa = (aa - 1) % 10 + 1
bb = (bb - 1) % 10 + 1

print((aa + bb))
