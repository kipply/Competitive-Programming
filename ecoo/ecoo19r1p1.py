import sys 
input = sys.stdin.readline

for _ in range(10): 
  n, m, d = map(int, input().split())
  days = [0 for _ in range(1001)]
  boop = list(map(int, input().split()))
  latest = 0 
  for i in range(m): 
    a = boop[i]
    days[a] += 1
    latest = max(latest, a)

  clean = n
  ans = 0 
  for day in range(1, d + 1):
    if clean == 0: 
      clean = n
      ans += 1 
    n += days[day]
    clean += days[day]
    clean -= 1 

  print ans
