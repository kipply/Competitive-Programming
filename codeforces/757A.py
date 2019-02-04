import sys
input = sys.stdin.readline 

b = "Bulbasr"
s = input().strip()

c = [s.count(x) for x in b]
c[1] /= 2
c[4] /= 2


print min(c)