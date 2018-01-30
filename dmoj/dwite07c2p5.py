import sys
input = sys.stdin.readline

def dfs(i):
    dead[i] = 1
    for j in range(1, n + 1):
        if cactus[i][j]:
            if not dead[j]:
                dfs(j)

for _ in range(5):
    n = int(input())
    m = int(input())
    cactus = [[0 for x in range(n + 1)] for x in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        cactus[a][b] = cactus[b][a] = 1
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if cactus[i][j]:
                cactus[i][j] = cactus[j][i] = 0
                dead = [0] * (n + 1)
                dfs(1);
                for k in range(1, n+ 1):
                    if not dead[k]:
                        ans += 1
                        break
                cactus[i][j] = cactus[j][i] = 1
    print ans
