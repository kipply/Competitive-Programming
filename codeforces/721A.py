import sys
input = sys.stdin.readline 

n = int(input())
s = input().strip()

a = [] 

c = 0 
for l in s: 
  if l is "B": 
    c += 1 
  if l is "W" and c: 
    a.append(c)
    c = 0 

if c: 
  a.append(c)
print(len(a))
print " ".join(map(str, a))