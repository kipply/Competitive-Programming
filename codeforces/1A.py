import sys, math, os
input = sys.stdin.readline

n, m, a = map(int, input().split())

print int(math.ceil(n / float(a)) * math.ceil(m / float(a)))
