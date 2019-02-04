import sys
input = sys.stdin.readline 

n = int(input())
l = list(map(int, input().split()))

max_l = max(l)
print(max(1, max_l - (sum(l) - max_l) + 1))
