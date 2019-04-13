import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())

def solve(n, p): 
  if n == a: 
    return p
  elif str(n)[-1] == "1" and len(str(n)) > 1: 
    return solve(int(str(n)[:-1]), p + [n])
  elif not n % 2: 
    return solve(n / 2, p + [n])
  else: 
    return False

ans = solve(b, [])
if not ans: 
  print "NO"
else: 
  print "YES" 
  print len(ans) + 1
  print str(a) + " " + " ".join(map(str, ans[::-1]))