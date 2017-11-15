n = int(input())
l = list(map(int, input().split(" ")))

print(" ".join(map(str,l)))
for a in range(n-1, 0, -1):
    for i in range(a):
        if l[i] > l[i+1]:
            t = l[i]
            l[i] = l[i+1]
            l[i+1] = t
            print(" ".join(map(str,l)))
