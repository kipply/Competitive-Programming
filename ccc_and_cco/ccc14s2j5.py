a = int(input())
b = input().split()
c = input().split()
f = True
for i in range(a):
    if b[i] == c[i]:
        print("bad")
        f = False
        break
    else:
        if c[i] != b[c.index(b[i])]:
            print("bad")
            f = False
            break
if f:
    print("good")
