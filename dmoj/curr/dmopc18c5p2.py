import sys
input = sys.stdin.readline 

n, m = map(int, input().split())

cactus = [list(map(float, input().split())) for _ in range(n)]

total = sum(sum(row) for row in cactus) 
avg = total / (n * m)

if round(avg, 6) == 0.48: 
  print "correctly exposed"
elif avg < 0.48: 
  lo = 1
  hi = 20000
  while lo < hi: 
    g = (hi + lo) / 2.0
    gg = sum(sum(min(col * g, 1) for col in row) for row in cactus) 
    if round(gg / (n * m), 9) > 0.48 : 
       hi = g - 0.0000000001
    else: 
      lo = g
  print "underexposed"
  print lo 

elif avg > 0.48: 
  print "overexposed"
  print 0.48 / avg
