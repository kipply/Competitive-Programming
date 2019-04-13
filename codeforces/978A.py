import sys, math, os
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))[::-1]
ans = list(set(a))[::-1]

print len(ans)
print " ".join(map(str, ans))