m = int(input())
n = int(input())
a = 0
for i in range(1, m + 1):
  for j in range(1, n + 1):
    if i + j == 10:
      a += 1
if a != 1:
  print("There are", a, "ways to get the sum 10.")
else:
  print("There is 1 way to get the sum 10.")
