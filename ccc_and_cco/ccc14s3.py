import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    curr = 1
    top = []
    branch = []
    for i in range(n):
        top.append(int(input()))
    ans = "Y"
    while curr < n:
        # print(curr, top, branch)
        if len(branch) and branch[-1] == curr:
            branch.pop()
            curr += 1
        elif len(top) and top[-1] == curr:
            top.pop()
            curr += 1
        elif len(top):
            branch.append(top.pop())
        else:
            ans = "N"
            break
    print ans
