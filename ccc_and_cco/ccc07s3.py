import sys
input = sys.stdin.readline
n = int(input())
friends = [-1 for x in range(10000)]
for i in range(n):
    x, y = map(int, input().split())
    friends[x] = y
x, y = map(int, input().split())
while x != 0 and y != 0:
    visited = [False for _ in range(10000)]
    d = -1
    while not visited[x] and x != y:
        visited[x] = True
        d += 1
        x = friends[x]
    if x == y:
        print("Yes", d)
    else:
        print("No")
    x, y = map(int, input().split())
