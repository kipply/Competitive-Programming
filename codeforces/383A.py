import sys
input = sys.stdin.readline 

n = int(input())
cows = list(map(int, input().split()))

cactus = [0 for _ in range(n + 1)]

for i in range(1, n + 1): 
  cactus[i] = cactus[i - 1] + cows[i - 1]

ans = 0 
for i in range(n): 
  if not cows[i]: 
    ans += cactus[i + 1]
print ans

