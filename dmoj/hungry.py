import sys
input = sys.stdin.readline

foodstuffs = []
n = int(input())
for i in range(n):
    foodstuffs.append(list(map(int, input().split())) + [i + 1])
print foodstuffs
foodstuffs.sort(key=lambda x: x[0])
print(" ".join(str(x[2]) for x in foodstuffs))
foodstuffs.sort(key=lambda x: x[1])
print(" ".join(str(x[2]) for x in foodstuffs))
