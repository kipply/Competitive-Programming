import sys
input = sys.stdin.readline 


k = int(input())
s = input().strip() 

d = {} 
for l in s: 
  if l not in d.keys(): 
    d[l] = 1
  else: 
    d[l] += 1

f = False
# print d
for i in range(1, len(s) + 1): 
  # print(i)
  if all(not d[x] % i for x in d.keys()) and i == k: 
    f = True
    root = ""
    for l in d.keys(): 
      root += l * (d[l] / i)
    print(root * i)
    break

if not f: 
  print -1