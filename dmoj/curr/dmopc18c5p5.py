import sys
input = sys.stdin.readline 

n = int(input())

peeps = [map(int, input().split()) for _ in range(n)][::-1]
hats = [p[0] for p in peeps]
wants = [p[1] for p in peeps]

ans = 1 << 30
def solve(line, unhappiness): 
  global ans
  print line, unhappiness
  if len(line) == 1: 
    unhappiness += abs(line[0][0] - line[0][1])
    ans = min(unhappiness, ans)
    return
  if unhappiness > ans: 
    return
  solve(line[1:], unhappiness + abs(line[0][0] - line[0][1]))
  print line
  unhappiness += abs(line[0][1] - line[1][0])  
  line[1][0] = line[0][0]
  solve(line[1:], unhappiness)    

solve(peeps, 0)
print ans