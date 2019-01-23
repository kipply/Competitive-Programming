import sys
k, m = map(int, sys.stdin.readline().split(" "))
b = 0
for i in range(pow(2, k)):
    b += sys.stdin.readline().strip().count("#")
print pow(pow(2, pow(4, m, 1000000006), 1000000007) - 1, b, 1000000007)
