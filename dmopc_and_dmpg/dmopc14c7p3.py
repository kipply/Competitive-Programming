import sys, math
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
cute = list(map(int, input().split()))
cute.extend(list(map(int, input().split())))
cute = set(cute)
print(n - (a + b - len(cute)))
