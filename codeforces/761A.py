import sys
input = sys.stdin.readline 

a, b = map(int, input().split())

if abs(b - a) < 2 and  not(not a and not b): 
  print "YES"
else: 
  print "NO"