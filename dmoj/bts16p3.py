n = int(input())
p = input().lower().split()
a = n
for i, person in enumerate(p):
    t = 0
    for j in range(i + 1, n):
        if person[0] == p[j][0]:
            t += 1
        else:
            break
    a += t
print(a)
