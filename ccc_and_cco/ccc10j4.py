import sys
input = sys.stdin.readline

while 1: 
  n = input().split()
  if n[0] == '0': 
    break

  a = list(map(int, n[1:]))
  n = int(n[0])

  d = [] 
  for i in range(1, n): 
    d.append(a[i] - a[i - 1])

  ans = len(d)

  for i in range(1, len(d)): 
    oop = [x for x in [d[l*i:min(len(d), l*i + i)] for l in range(0, len(d))]]
    try: 
      oop = filter(None, oop)
    except: 
      pass
    if len(set([str(x) for x in oop])) == 1: 
      ans = i
      break
    if len(set([str(x) for x in oop][:-1])) == 1 and oop[-1] == oop[0][:len(oop[-1])]: 
      ans = i 
      break


  print ans
