import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

snowmen = list(map(int, input().split()))

a_min = 1
a_max = 2 * (10 ** 9)

def valid(g):
    k_count = 0
    da = [0] * (n + 1)
    for i in range(n):
        da[i] += 0 if i == 0 else da[i - 1]
        curr = snowmen[i] + da[i]
        if curr < a_guess:
            diff = g - curr
            k_count += diff
            if k_count > k:
                return False
            da[i] += diff
            da[min(n, i + m)] -= diff
    return True

while a_min < a_max:
    a_guess = (a_max + a_min + 1) / 2
    if valid(a_guess):
        a_min = a_guess
    else:
        a_max = a_guess - 1
print a_min
