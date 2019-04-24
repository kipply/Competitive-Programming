import sys
input = sys.stdin.readline 


n = int(input()) 
lines = [0] 

for i in range(n): 
  lines.append(input().split()) 

m = int(input()) 
match = [] 

for i in range(m): 
  match.append(int(input()))

valid = [True for _ in range(n + 1)]
for num in match: 
  for i in range(1, n + 1): 
    line = lines[i]
    if not valid[i]: continue
    
    if lines[i][0] == "PRINT": 
      if num != int(lines[i][1]): 
        valid[i] = False 
        break

    elif lines[i][0] == "GOTO": 
      v = [False for _ in range(n + 1)]
      while line[0] == "GOTO": 
        dest = int(line[1])
        if (v[dest]): 
          valid[i] = False
          break
        v[int(line[1])] = True
    else: 
      valid[i] = False
for i in range(1, n + 1): 
  line = lines[i]
  if not valid[i]: continue
  
  if lines[i][0] == "PRINT": 
    valid[i] = False
  elif lines[i][0] == "GOTO": 
    v = [False for _ in range(n + 1)]
    while line[0] == "GOTO": 
      dest = int(line[1])
      if (v[dest]): 
        valid[i] = False
        break
      v[int(line[1])] = True

ans = [] 
for i in range(1, n + 1): 
  if valid[i]: 
    ans.append(i)
print " ".join(map(str, sorted(ans)))
