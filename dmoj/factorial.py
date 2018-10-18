def f(a):
    aa = 1
    for j in range(1, a + 1):
        aa = aa * j % (2**32)
    return aa
n = int(input())
for i in range(n):
    nn = int(input())
    if nn > 50:
        print(0)
    else:
        print(f(nn))
