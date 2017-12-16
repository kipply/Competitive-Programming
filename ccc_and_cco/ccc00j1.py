a = input()
b = int(a.split(" ")[1])
a = int(a.split(" ")[0])

print("Sun Mon Tue Wed Thr Fri Sat")
counter = a - 1
for i in range(1, a):
  print("    ", end="")
for i in range(1, b + 1):
  counter += 1
  if counter == 7:
    counter = 0
    if i < 10:
      print("  " + str(i) + " ")
    else:
      print(" " + str(i) + " ")
  else:
    if i < 10:
      print("  " + str(i) + " ", end="")
    else:
      print(" " + str(i) + " ", end="")
