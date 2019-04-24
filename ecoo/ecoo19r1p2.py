import sys 
input = sys.stdin.readline

for _ in range(10): 
  boop = input().split() 
  r = int(boop[0])
  t = int(boop[1])
  a = boop[2].strip()

  cute = {}
  for i in range(r): 
    c, b = input().split() 
    c = c.strip() 
    b = b.strip() 
    cute[c] = b

  ans = 0 
  first = a[0]
  second = a[-1]
  curr = {}
  for l in cute.keys(): 
    if l in a: 
      curr[l] = a.count(l)
    else: 
      curr[l] = 0

  for i in range(t): 
    first = cute[first][0]
    second = cute[second][-1]
    change = {}
    for ll in cute.keys(): change[ll] = 0 

    for l in curr.keys(): 
      for replacement_l in cute[l]: 
        change[replacement_l] += curr[l] 

    curr = change.copy()

  print(first + second + " " + str(sum(curr.values())))
  
