import sys

n = int(sys.stdin.readline())
contestants = {} # dictionary
for i in range(n * 2 - 1):
    name = sys.stdin.readline()
    if not name in contestants:
        contestants[name] = 0
    contestants[name] += 1

# print(contestants)
for name in contestants.keys():
    if contestants[name] % 2 == 1:
        print(name)
        break
