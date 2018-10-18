import math
n = int(input())
for i in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    p = ( a + b + c ) / 2
    print(math.sqrt( p * ( p - a) * ( p - b) * ( p - c) ), a + b + c)
