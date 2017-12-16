a = int(input())
b = int(input())
c = 1
while b >= 0:
  d = a - b
  a = b
  b = d
  c += 1
print(c)
