import sys
input = sys.stdin.readline 

cactus = [[False for _ in range(51)] for _ in range(51)]
init = [
  (1, 6), 
  (2, 6), 
  (6, 7), 
  (5, 6), 
  (4, 6), 
  (3, 4),
  (4, 5),
  (3, 6), 
  (3, 5), 
  (6, 7), 
  (3, 15), 
  (13, 15), 
  (12, 13), 
  (13, 14), 
  (16, 17), 
  (17, 18), 
  (16, 18), 
  (12, 13), 
  (7, 8), 
  (8, 9), 
  (9, 12), 
  (9, 10), 
  (10, 11), 
  (11, 12)
]

for pair in init: 
  cactus[pair[0]][pair[1]] = True
  cactus[pair[1]][pair[0]] = True

while True: 
  command = input().strip()
  if command is 'q': break

  if command is "i": 
    x = int(input())
    y = int(input())

    cactus[x][y] = True
    cactus[y][x] = True

  if command is "d": 
    x = int(input())
    y = int(input())

    cactus[x][y] = False
    cactus[y][x] = False 

  if command is "n": 
    x = int(input())

    print(sum(cactus[x]))
    
  if command is "f": 
    x = int(input())
    ans = set()
    fs = set()
    fs.add(x)
    for i in range(51): 
      if cactus[x][i]:
        fs.add(i)
        for j in range(51): 
          if cactus[i][j]: 
            ans.add(j)
    print len(ans - fs) 

  if command is "s": 
    x = int(input())
    y = int(input())
    q = [x, None] 
    v = [False for _ in range(51)]
    ans = 0 
    while q: 
      # print(q)
      curr = q.pop(0)
      if curr is None: 
        ans += 1 
        q.append(None)
        if q[0] is None: 
          ans = "Not connected"
          break
        continue
      if curr is y: 
        break
      if v[curr]: continue
      v[curr] = True 
      for f in range(51): 
        if cactus[curr][f]: 
          q.append(f)
    print ans
