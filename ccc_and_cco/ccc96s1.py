n = int(input())
for i in range(n):
  a = []
  b = int(input())
  for i in range(1, b):
    if b % i == 0:
      a.append(i)
  if sum(a) > b:
    print(b, "is an abundant number.")
  elif sum(a) < b:
    print(b, "is a deficient number.")
  else:
    print(b, "is a perfect number.")
