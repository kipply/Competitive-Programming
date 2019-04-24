import sys
input = sys.stdin.readline

n, m = map(int, input().split())
members = list(map(int, input().split()))

cute = {}

for i in range(m): 
  a, b, c = input().split()
  b = int(b)
  c = int(c) 
  if a == "T": 
    for teamsize in range(n + 1): 
      
      if (b - teamnumber) %  teamsize == 0: 

  if (str(b) +  " " + str(c) not in cute): 
    ans = 0 
    for j in range(c - 1, n, b): 
      # print(members[j], c)
      ans += members[j]
    cute[str(b) +  " " + str(c)] = ans 
  else : 
    ans = cute[str(b) +  " " + str(c)]
  print ans

