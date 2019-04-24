import sys 
input = sys.stdin.readline

for _ in range(10): 
  j, w, h = map(int, input().split())
  cactus = [] 
  start = 0 
  end = 0 
  for i in range(h):
    row = list(input().strip())
    cactus.append(row)
    for x in range(w): 
      if row[x] == 'L': 
        start = (i, x)
      if row[x] == 'G': 
        end = (i, x)

  ans = "CLEAR"

  while True: 
    if cactus[start[0]][start[1] + 1] is ".": 
      start = (start[0], start[1] + 1) 
    elif cactus[start[0]][start[1] + 1] is "@": 

      # check if it's low enough
      wallheight = 0
      for i in range(h - 2, -1, -1):
        if cactus[i][start[1] + 1] == "@": 
          wallheight += 1 
        else: 
          break

      if wallheight == h - 1 or j < wallheight: 
        ans = start[1] + 1
        break

      for i in range(start[0], h - 2 - wallheight, -1): 
        if cactus[i][start[1]] == "@" or cactus[i][start[1] + 2] == "@": 
          ans = start[1] + 1
          break
      if ans != "CLEAR": break

      start = (start[0], start[1] + 2)
    elif cactus[start[0]][start[1] + 1] is "#" or cactus[start[0]][start[1] + 1] is "L": 
      print "Carol wtf"
    else: # G
      break

  if ans != "CLEAR": 
    ans += 1
  print ans 
  input()
