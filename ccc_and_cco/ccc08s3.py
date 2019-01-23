import sys

input = sys.stdin.readline 

t = int(input())
for cute in range(t): 
  r = int(input())
  c = int(input())
  cactus = ["" for _ in range(r)]
  for i in range(r): 
    cactus[i] = list(input().strip())

  q = [(0, 0), None]
  dr = [0, 0, -1, 1]
  dc = [-1, 1, 0, 0]

  ans = 1
  while True: 
    if q[0] == None:
      ans += 1
      q.pop(0)
      q.append(None)
      if len(q) == 1 or q[1] == None: 
        ans = -1
        break 

      continue

    curr_r, curr_c = q.pop(0)

    if curr_r < 0 or curr_c < 0 or  curr_r >= r or curr_c >= c or cactus[curr_r][curr_c] == '#':  
      continue
    elif cactus[curr_r][curr_c] == '*': 
      cactus[curr_r][curr_c] = '#'
      continue
    elif curr_r == r - 1 and curr_c == c - 1: 
      break
    elif cactus[curr_r][curr_c] == '+': 
      cactus[curr_r][curr_c] = '#'
      for i in range(4): 
        q.append((curr_r + dr[i], curr_c + dc[i]))
    elif cactus[curr_r][curr_c] == '-': 
      cactus[curr_r][curr_c] = '#'
      q.append((curr_r + dr[0], curr_c + dc[0]))
      q.append((curr_r + dr[1], curr_c + dc[1]))
    elif cactus[curr_r][curr_c] == '|': 
      cactus[curr_r][curr_c] = '#'
      q.append((curr_r + dr[2], curr_c + dc[2]))
      q.append((curr_r + dr[3], curr_c + dc[3]))
    else: 
      if q[0] == None: 
        ans = -1
        break 
      ans += 1
      q.append(None)

  print ans