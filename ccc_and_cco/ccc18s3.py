import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cactus = [None for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for i in range(n):
  cactus[i] = list(input().strip())
  try: sr, sc = i, cactus[i].index("S")
  except: pass

for r in range(n):
  for c in range(m):
    if cactus[r][c] is "C":
      for cute in [range(r + 1, n), range(r - 1, -1, -1)]: 
        for k in cute: 
          if cactus[k][c] is "W": break
          if cactus[k][c] == "S": 
            cactus[k][c] = 0
          if cactus[k][c] == ".": 
            cactus[k][c] = -1
      for cute in [range(c + 1, m), range(c - 1, -1, -1)]: 
        for k in cute: 
          if cactus[r][k] is "W": break
          if cactus[r][k] == "S": 
            cactus[r][k] = 0
          if cactus[r][k] == ".": 
            cactus[r][k] = -1
      cactus[r][c] = "W"

    # if cactus[r][c] in list("LRUD"): 
    #   cactus[r][c] = conveyor(r, c)

# for row in casctus: print row
q = [(sr, sc), None]
distance = 1

global conveyor
def conveyor(r, c, v=[]): 
  global conveyor
  if cactus[r][c] == "L": 
    d = 1
  elif cactus[r][c] == "R": 
    d = 0
  elif cactus[r][c] == "U": 
    d = 2
  else: 
    d = 3
  if (r, c) in v: return
  next_ = cactus[r + dr[d]][c + dc[d]]
  if next_ in list("LRUD"): 
    res = conveyor(r + dr[d], c + dc[d], v + [(r, c)])
    return res
  elif next_ == '.': 
    return (r + dr[d], c + dc[d])
  else: 
    return ()

while q:
  if q[0] is None:
    distance += 1
    q.pop(0)
    q.append(None)
    if q[0] is None : break
    continue
  r, c = q.pop(0)
  if cactus[r][c] in ["W", -1, 0]: continue

  for d in range(4):
    nr, nc = r + dr[d], c + dc[d]
    if nr > n or nc > m: continue
    if cactus[nr][nc] == ".":
      cactus[nr][nc] = distance
      q.append((nr, nc))

    if cactus[nr][nc] in list("LRUD"): 
      if conveyor(nr, nc): 
        rr, rc = conveyor(nr, nc)
        cactus[rr][rc] = distance
        q.append((rr, rc))
      cactus[nr][nc] = 0

for r in range(n):
    for c in range(m):
        if cactus[r][c] == '.': 
          print -1
        elif type(cactus[r][c]) is int and cactus[r][c]: 
          print(cactus[r][c])
