n = int(input())
m = int(input())
f = True
for i in range(1, m + 1):
    if (n * i - 1) % m == 0:
        print(i)
        f = False
if f:
    print("No such integer exists.")
