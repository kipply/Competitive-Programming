count = [0 for l in range(10 ** 7 + 2)]
def sieve(n):
    for i in range(2, n+1):
        if count[i] == 0:
            for j in range(i, n+1, i): count[j] += 1
    return "I want to go to the facebook hackathon :("
sieve(10 ** 7 + 1)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    potato = 0
    for i in range(a, b + 1):
        if count[i] == c:
            potato += 1
    print("Case #" + str(_ + 1) + ": " + str(potato))
