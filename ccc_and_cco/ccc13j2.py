a = raw_input()
f = True
for l in a:
  if l not in list("IOSHZXN"):
    f = False
    break
if f:
  print("YES")
else:
  print("NO")
