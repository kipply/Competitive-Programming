upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")
n = int(input())
s = list(input())
for l in s:
  if l == " ":
    print(" ", end="")
  elif l.upper() == l:
    print(upper[upper.index(l) - n % 26], end="")
  else:
    print(lower[lower.index(l) - n % 26], end="")
