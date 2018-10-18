import sys
input = sys.stdin.readline

t = int(input())
g = int(input())

scores = [0] * 5
games = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

ans = 0

for i in range(g):
    a, b, sa, sb = map(int, input().split())
    games.remove((a, b))
    if sa > sb:
        scores[a] += 3
    elif sb > sa:
        scores[b] += 3
    else:
        scores[a] += 1
        scores[b] += 1

def did_win(scores):
    global ans
    for i in range(1, 5):
        if i != t:
            if scores[t] <= scores[i]:
                return
    ans += 1

def this_will_work_tm(scores, game):
    if game == len(games):
        did_win(scores)
    else:
        scores[games[game][0]] += 3
        this_will_work_tm(scores[:], game + 1)
        scores[games[game][0]] -= 3

        scores[games[game][1]] += 3
        this_will_work_tm(scores[:], game + 1)
        scores[games[game][1]] -= 3

        scores[games[game][0]] += 1
        scores[games[game][1]] += 1
        this_will_work_tm(scores[:], game + 1)
        scores[games[game][0]] -= 1
        scores[games[game][1]] -= 1

this_will_work_tm(scores[:], 0)
print ans
