n = int(input())
for i in range(n):
    a = int(input())
    b = 2
    while b * b <= a:
        while a % b == 0:
            a = a / b
            print(b, end=" ")
        b = b + 1
    if a > 1:
        print(int(a))
    else:
        print("")
