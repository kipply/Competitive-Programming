q = int(input())
a = int(input())
b = int(input())
c = int(input())
ans = 0
machine = 0
while q != 0:
    q = q - 1
    if machine == 0:
        a += 1
        if a == 35:
            q += 30
            a = 0

    elif machine == 1:
        b += 1
        if b == 100:
            q += 60
            b = 0

    elif machine == 2:
        c += 1
        if c == 10:
            q += 9
            c= 0
    if machine == 2:
        machine = 0
    else:
        machine += 1
    ans += 1
print("Martha plays " + str(ans) + " times before going broke.")
