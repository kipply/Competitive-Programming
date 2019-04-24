import sys
input = sys.stdin.readline

t = int(input())
for C in range(1, t + 1): 
  n = int(input())
  p = sorted(list(map(float, input().split())))[::-1]
  ans = 1 
  for i in range(n): 
    ans *= (1 - p[i] * p[-i -1])
    # print( p[i] *p[-i -1])

  print "Case #" + str(C) + ": " + str(ans)

