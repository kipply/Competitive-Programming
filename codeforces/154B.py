import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
divisors = [[] for _ in xrange(n + 1)]

colliders = [0 for _ in xrange(n + 1)]

nd = [[] for i in xrange(n + 1)]
for i in xrange(2, n + 1, 2): nd[i] = [2]
for i in xrange(3, n + 1, 2):
    if nd[i]: continue
    for j in xrange(i, n + 1, i): nd[j].append(i)

for _ in xrange(m): 

  command, k = input().split()
  k = int(k)

  if command == "+": 
    if colliders[k]: 
      print "Already on"
    else: 
      f = True
      for d in nd[k]: 
        if len(divisors[d]): 
          f = False
          d = divisors[d][0]
          break
      if f: 
        for d in nd[k]: 
          divisors[d].append(k)
        colliders[k] = 1
        print "Success"
      else: 
        print "Conflict with " + str(d)
  else: 
    if colliders[k]: 
      colliders[k] = 0 
      for d in nd[k]: 
        divisors[d].remove(k)
      print "Success"
    else: 
      print "Already off"