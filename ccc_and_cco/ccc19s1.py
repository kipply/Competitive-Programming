import sys 
input = sys.stdin.readline

s = input().strip()

cactus = [[1, 2], [3, 4]]

while "VV" in s or "HH" in s: 

  s = s.replace("VV", "")
  s = s.replace("HH", "")

for l in s:
  if l is "V": 
    t = [x[0] for x in cactus]
    for i in range(2): 
      cactus[i][0] = cactus[i][1]
      cactus[i][1] = t[i]
  elif l is "H": 
    t = cactus[0] 
    cactus[0] = cactus[1] 
    cactus[1] = t

for row in cactus: 
  print(" ".join(map(str, row)))
