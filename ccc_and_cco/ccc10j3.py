x = "0"
a = 0
b = 0
while 1:
  x = input().split(" ")
  x[0] = int(x[0])
  if x[0] == 1:
    if x[1] == "A":
      a = int(x[2])
    else:
      b = int(x[2])
  elif x[0] == 2:
    if x[1] == "A":
      print(a)
    else:
      print(b)
  elif x[0] == 3:
    if x[1] == "A" and x[2] == "B":
      a = a + b
    elif x[1] == "A" and x[2] == "A":
      a = a * 2
    elif x[1] == "B" and x[2] == "B":
      b = b * 2
    elif x[1] == "B" and x[2] == "A":
      b = a + b
  elif x[0] == 4:
    if x[1] == "A" and x[2] == "B":
      a = a * b
    elif x[1] == "A" and x[2] == "A":
      a = a * a
    elif x[1] == "B" and x[2] == "B":
      b = b * b
    elif x[1] == "B" and x[2] == "A":
      b = a * b
  elif x[0] == 5:
    if x[1] == "A" and x[2] == "B":
      a = a - b
    elif x[1] == "A" and x[2] == "A":
      a = 0
    elif x[1] == "B" and x[2] == "B":
      b = 0
    elif x[1] == "B" and x[2] == "A":
      b = b - a
  elif x[0] == 6:
    if x[1] == "A" and x[2] == "B":
      a = a // b
    elif x[1] == "A" and x[2] == "A":
      a = 1
    elif x[1] == "B" and x[2] == "B":
      b = 1
    elif x[1] == "B" and x[2] == "A":
      b = b // a
  else:
    break;
