import sys
import re
input = sys.stdin.readline
num_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def to_roman(num):
    roman = ''
    while num > 0:
        for i, r in num_roman:
            while num >= i:
                roman += r
                num -= i
    return roman

def from_roman(num):
    s = 0

    for l, v in [("IX", 9), ("IV", 4), ("XL", 40), ("CD", 400), ("XC", 90)]:
        if l in num:
            num = re.sub(l, '' , num)
            s += v

    for v, l in num_roman:
        s += num.count(l) * v;
    return s
n = int(input())
for i in range(n):
    a, b = input().rstrip()[:-1].split('+')
    ans = from_roman(a) + from_roman(b)
    if ans < 1000:
        print(a + "+" + b + "=" + to_roman(ans))
    else:
        print(a + "+" + b + "=" + "CONCORDIA CUM VERITATE")
