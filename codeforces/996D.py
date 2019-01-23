import sys
input = sys.stdin.readline

n = int(input())
cutes = list(map(int, input().split()))
count = 0
def swap(s, t):
    global count
    global cutes
    for j in range(s, n * 2):
        if cutes[j + 1] == t:
            break
        temp = cutes[j + 1]
        cutes[j + 1] = cutes[j]
        cutes[j] = temp
        count += 1
    del cutes[j: j+2]
while cutes:
    if cutes[0] != cutes[1]:
        swap(0, cutes[0])
    else:
        cutes = cutes[2:]
print count
