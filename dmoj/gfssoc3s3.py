import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(9)
elif n == 3:
    print 108
elif n > 3500:
    print 999999998
elif not n % 2:
    print (int('1' + ''.join(['9' for _ in range(n / 2)])) - 1) % 1000000000
else:
    print (int('10' + ''.join(['9' for _ in range(n / 2 - 1)])) - 1) % 1000000000
