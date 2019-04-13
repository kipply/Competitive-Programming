import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())

print max(0, n - (k - (2 * n)))