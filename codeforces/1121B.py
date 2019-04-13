import sys 
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cactus = [0 for _ in range(10 ** 5 * 2 + 1)]

for i in range(n): 
  for j in range(i + 1, n): 
    cactus[a[i] + a[j]] += 1 

print max(cactus)