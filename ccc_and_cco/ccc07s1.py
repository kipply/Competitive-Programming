#### DO NOT COPY THIS BOIIII I'M WATCHING
for _ in range(int(input())):
    y, m, d = map(int, input().split())
    if (2007 - y > 18) or (2007 - y == 18 and 2 - m > 0) or (2007 - y == 18 and  2 - m == 0 and 27 - d >= 0):
        print("Yes")
    else:
        print("No")
