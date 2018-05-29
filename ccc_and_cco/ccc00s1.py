import sys
input = sys.stdin.readline
out = sys.stdout.write

a, b = map(int, input().split())
out("Sun Mon Tue Wed Thr Fri Sat\n")
counter = a - 1
for i in range(1, a):
  out("    ")
for i in range(1, b + 1):
  counter += 1
  if counter == 7 or i == b:
    counter = 0
    if i < 10:
      out("  " + str(i) + "\n")
    else:
      out(" " + str(i) + "\n")
  else:
    if i < 10:
      out("  " + str(i) + " ")
    else:
      out(" " + str(i) + " ")
