import sys, math
input = sys.stdin.readline

n = int(input())

bills = [100, 20, 10, 5, 1]
def f(bills, kevin):
    res = 0
    for b in bills:
        if kevin % b == 0:
            res += kevin / b
            return res
        else:
            res += math.trunc(kevin / float(b))
            kevin -= (b * math.trunc(kevin / float(b)))

print(f(bills, n))
