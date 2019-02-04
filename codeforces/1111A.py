import sys
input = sys.stdin.readline 

s = input().strip()
t = input().strip()

vowels = list("aeiou")

ans = "Yes" 
if len(s) != len(t): 
  ans = "No"
else: 
  for i in range(len(s)): 
    if s[i] in vowels and t[i] not in vowels: 
      ans = "No"
    if s[i] not in vowels and t[i] in vowels: 
      ans = "No" 

print ans

