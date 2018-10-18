e, n = input().split()
a = input().split()[::-1]
a.append(e)

b = 10
for i in a:
    if b - 1:
        b = int(i, b)
    else:
        b = str(i).count('1')

print(b)
