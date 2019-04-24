import sys
input = sys.stdin.readline

t = int(input())
for C in range(1, t + 1): 
  f, s = map(int, input().split())
  friends = sorted([map(int, input().split()) for _ in range(f)])
  rows = [0 for _ in range(101)] 
  for i in range(f - 1): 
    if friends[i] != friends[i + 1]: 
      if friends[i][0] == friends[i][1]: 
        rows[friends[i][0]] += 1
      else: 
        rows[friends[i][0]] += 1
        rows[friends[i][1]] += 1

  rows[friends[-1][0]] += 1
  if friends[-1][0] != friends[-1][1]: 
    rows[friends[-1][1]] += 1

  # print friends, rows
  print "Case #" + str(C) + ": " + str(max(rows))