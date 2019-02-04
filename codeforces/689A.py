import sys
input = sys.stdin.readline 

n = int(input())

m = [list("123")] + [list("456")] + [list("789")] + [[False, "0", False]]


digits = list(input().strip())

digits_m = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for d in digits: 
  for i in range(4): 
    for j in range(3): 
      if d == m[i][j]: 
        digits_m.append((i, j))
ans = "YES"
for i in range(4): 
  cuteness = []
  for r, c in digits_m: 
    try: 
      validations = [
        r + dr[i] >= 0 and m[r + dr[i]][c],
        c + dc[i] >= 0 and m[r][dc[i] + c]
      ]
      if all(validations): 
        cuteness.append(True)
      else: 
        cuteness.append(False) 
    except: 
      cuteness.append(False) 
  if all(cuteness): 
    ans = "NO"

print ans