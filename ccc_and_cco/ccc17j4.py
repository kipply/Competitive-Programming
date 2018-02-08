import sys
input = sys.stdin.readline

n = int(input())
t = 1200
a = 0
a = (n / 720) * 31
n = n % 720
for i in range(n + 1):
    tt = str(t)
    # mmmm delicious spaghetti code
    if len(tt) == 3:
        if int(tt[0]) - int(tt[1]) == int(tt[1]) - int(tt[2]):
            a += 1
    else:
        if int(tt[0]) - int(tt[1]) == int(tt[1]) - int(tt[2]) and int(tt[1]) - int(tt[2]) == int(tt[2]) - int(tt[3]):
            a += 1
    t += 1
    if (t % 100) >= 60:
        t += 100
        t -= 60

    # hours
    if t >= 1300:
        t -= 1200


print a
