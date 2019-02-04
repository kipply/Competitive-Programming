import sys
input = sys.stdin.readline 

n = int(input())


for x in range(n, -1, -1):
  if x / 2.0 * (x + 1) <= n: 
    if x: 
      print x
    else: print 1
    print " ".join(map(str, [i for i in range(1, x)] + [int(x + n - (x / 2.0 * (x + 1)))]))
    break