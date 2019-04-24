import sys
input = sys.stdin.readline

t = input().strip()
n = len(t) 

try: 
  last_a = n - t[::-1].index('a') - 1
except: 
  last_a = 0
non_a = t[:last_a].replace('a', '')

curr_split = last_a + 1

if (last_a == 0 and t[0] != 'a'): 
  curr_split = 0

f = False
# print non_a, curr_split, t[curr_split:]
for i in range(last_a, n): 
  if non_a == t[curr_split:]: 
    print t[:curr_split]
    f = True
    break 
  elif curr_split < n: 
    non_a += t[curr_split] 
    curr_split += 1
  # print non_a, curr_split, t[curr_split:]

if not f: 
  print ":("