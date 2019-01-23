import sys
input = sys.stdin.readline

dordor = list(input().strip())
ans = "NO"
for i in range(1, len(dordor)):
    # print(dordor[:i], dordor[i:])
    if dordor[:i][::-1] == dordor[:i] and dordor[i:] == dordor[i:][::-1]:
        ans = "YES"
        break

print ans
