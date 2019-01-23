import sys
input = sys.stdin.readline 

n = int(input())
l = list(map(int, input().split()))


while len(set(l)) > 1: 
  for i in range(n): 
    for j in range(n): 
      if l[i] > l[j]: 
        l[i] -= l[j]
      elif l[j] > l[i]: 
        l[j] -= l[i]

print(sum(l))