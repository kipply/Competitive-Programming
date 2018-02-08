import sys
n, k, d = map(int, sys.stdin.readline().split())
jacks = []
dusts = [0] * n
for i in range(n):
  dusts[i] = sys.stdin.readline().strip()
jacks = []
dustness = 1
for i in range(n - 1, -1, -1):
  if dustness > d:
    jacks.extend(["dust"] * dusts[:i + 1].count("T"))
    break
  elif dusts[i] == "T":
    jacks.append(dustness)
  else:
    dustness *= int(dusts[i].split()[1])
for j in jacks[::-1]:
  print(j)
