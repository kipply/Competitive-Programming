import sys
input = sys.stdin.readline

n = int(input())
adj = [set() for _ in range(n + 1)]
dp_question_mark = [0 for _ in range(n + 1)]
x, y = map(int, input().split())
while x != 0:
    adj[x].add(y)
    x, y = map(int, input().split())

dp_question_mark[1] = 1
for brian_is_cute in range(n + 1):

    for cactus in adj[brian_is_cute]:
        dp_question_mark[cactus] += dp_question_mark[brian_is_cute]
print(dp_question_mark[n])
