import sys
input = sys.stdin.readline
n = int(input())
print "NO" if n % 2 or n < 0  else "YES"
