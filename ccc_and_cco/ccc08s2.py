import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n: break
    cust = n
    for i in range(1, n):
        cust += int((n * n - i * i) ** 0.5)
    print(cust * 4 + 1)
