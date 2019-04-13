import sys
input = sys.stdin.readline 

n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))


ans = (a[-1] * k + a[-2]) * (m / (k+ 1)) + ((m % (k + 1)) * a[-1])
print ans
