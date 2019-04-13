import sys, math, os
input = sys.stdin.readline

na, nb = map(int, input().split())
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = "NO"
# print (a[:k][-1], b[::-1][:m][-1])
# print(a[::-1][:k][0], b[:m][0])
if a[:k][-1] < b[::-1][:m][-1] or a[::-1][:k][0] < b[:m][0]: 
  ans = "YES"

print ans