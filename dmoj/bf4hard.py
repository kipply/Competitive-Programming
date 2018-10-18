#knuth morris pratt algorithm
import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline() .rstrip()
def rkm(text, pattern, pr):
    n = len(text)
    m = len(pattern)
    h = pow(31, m - 1) % pr
    p = 0
    t = 0
    res = -1
    for i in range(m):
        p = (31 * p + ord(pattern[i])) % pr
        t = (31 * t + ord(text[i])) % pr
    for s in range(n - m + 1):
        if p == t:
            f = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    f = False
                    break
            if f:
                res = s
                break
        if s < n - m:
            t = (t - h * ord(text[s])) % pr
            t = (t * 31 + ord(text[s+m])) % pr
            t = (t + pr) % pr
    return res
print(rkm(a, b, 1000000007))
