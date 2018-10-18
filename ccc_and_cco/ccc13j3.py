a = int(input()) + 1
for i in range(a):
    if not set([x for x in list(str(a)) if list(str(a)).count(x) > 1]):
        print(a)
        break
    a += 1
