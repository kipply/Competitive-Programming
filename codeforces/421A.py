import sys
import itertools
input = sys.stdin.readline 

n, a, b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
for i in range(1, n + 1): 
  if i in a: 
    ans.append('1')
  else: 
    ans.append('2')

print " ".join(ans)

