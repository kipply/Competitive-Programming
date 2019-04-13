import sys, math, os
input = sys.stdin.readline

n, m = map(int, input().split())
measures = [map(int, input().split()) for _ in range(m)]
ans = measures[0][1] + measures[0][0] - 1
for i in range(1, m): 
  if measures[i][0] - measures[i - 1][0] < abs(measures[i][1] - measures[i - 1][1]): 
    ans = "IMPOSSIBLE"
    break
  else: 
    d_days = measures[i][0] - measures[i - 1][0]
    d_depth = measures[i][1] - measures[i - 1][1] 

    ans = int(max(ans, measures[i][1], 
      (d_days - abs(d_depth)) / 2 + max(measures[i - 1][1], measures[i][1])))

ans = max(ans, measures[-1][1] + n - measures[-1][0]) 
print ans
