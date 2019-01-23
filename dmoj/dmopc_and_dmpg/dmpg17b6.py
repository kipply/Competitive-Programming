import math
a = input()
a = list(map(int, raw_input().split(" ")))
b = 0
for i in a:
    b += math.log(i, 2)
print(int(b + 1))
