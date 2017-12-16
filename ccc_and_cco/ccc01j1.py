h = int(input())
for i in range(1,h, 2):
  for j in range(0,i):
    print("*", end="")
  for j in range(0, h*2 - i*2):
    print(" ", end="")

  for j in range(0,i):
    print("*", end="")
  print("")
for i in range(h, 0, -2):
  for j in range(0,i):
    print("*", end="")
  for j in range(0, h*2 - i*2):
    print(" ", end="")

  for j in range(0,i):
    print("*", end="")
  if i != 1:
    print("")
