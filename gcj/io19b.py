import sys, random
input = sys.stdin.readline

t = int(input())

# for i in range(100): 
#   x = random.randint(1, 100)
#   y = random.randint(1, 100)

#   print x, y, random.randint(0, x * y)
for C in range(1, t + 1): 
  r, c, k = map(int, input().split())
  cactus = [["*" for _ in range(c)] for _ in range(r)]
  possible = "POSSIBLE"
  curr = [0, 0]
  for i in range(k): 
    cactus[curr[0]][curr[1]] = "N"
    if curr[1] == c - 1: 
      curr = [curr[0] + 1, 0]
    else: 
      curr = [curr[0], curr[1] + 1]

  while k != r * c: 
    # print curr
    if r > 1 and curr[0] != r - 1: 
      cactus[curr[0]][curr[1]] = "S"
    elif r == 1 and curr[1] != c - 1: 
      cactus[curr[0]][curr[1]] = "E"
    elif r == 1 and curr[1] == c - 1 and r > 1:
      if curr[0] == 0 or cactus[curr[0]][curr[1] - 1] == "N": 
        # print"TH"
        possible = "IMPOSSIBLE" 
        break
      cactus[curr[0]][curr[1]] = "W"
    elif curr[0] == r - 1 and curr[1] != c - 1: 
      if curr[1] == c - 1 or cactus[curr[0]][curr[1] + 1] == "N": 
        possible = "IMPOSSIBLE"
        break
      cactus[curr[0]][curr[1]] = "E"
    elif curr[0] == r - 1 and curr[1] == c - 1: 
      if curr[1] == 0 or cactus[curr[0]][curr[1] - 1] == "N": 
        if cactus[curr[0] - 1][curr[1]] == "S": 
          cactus[curr[0]][curr[1]] = "N"
          break
        possible = "IMPOSSIBLE"
        break
      cactus[curr[0]][curr[1]] = "W"

    if curr[1] == c - 1: 
      curr = [curr[0] + 1, 0]
      if curr[0] == r: 
        break
    else: 
      curr = [curr[0], curr[1] + 1]

  print "Case #" + str(C) + ": " + possible
  if possible == "POSSIBLE": 
    for row in cactus: print "".join(row)