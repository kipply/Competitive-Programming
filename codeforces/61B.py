import sys
import itertools
input = sys.stdin.readline 

s = [input().strip().replace(';', '').replace('-', '').replace('_', '').lower() for _ in range(3)]

n = int(input())

for i in range(n): 
  c = input().strip().replace(';', '').replace('-', '').replace('_', '').lower()
  f = "WA"  
  if any("".join(x) == c for x in list(itertools.permutations(s, 3))): 
    f = "ACC"
  print f 