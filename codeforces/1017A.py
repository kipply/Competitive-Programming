import sys
input = sys.stdin.readline 

n = int(input())
cute = [] 
for i in range(n): 
  cute.append((-sum(map(int, input().split())), i))

cute.sort()
for i in range(n): 
  if not cute[i][1]: 
    print i + 1