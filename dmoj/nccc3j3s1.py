import sys
from collections import Counter
input = sys.stdin.readline

dordor = list(input().rstrip())
dordor.sort()
dordor.sort(key=Counter(dordor).get)
ans = 0
while len(set(dordor)) > 2:
    dordor.pop(0)
    ans += 1

print ans