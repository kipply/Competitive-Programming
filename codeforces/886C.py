import sys, math, os
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

ans = len(t) - len(set(t)) + 1 
print ans