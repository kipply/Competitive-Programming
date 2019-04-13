import sys 
input = sys.stdin.readline

n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
ans = 0
for chosen in c: 
  if any(p[x] > p[chosen - 1] and s[x] == s[chosen - 1] for x in range(n)): 
    ans += 1 
    p[chosen - 1] = -1 

print ans