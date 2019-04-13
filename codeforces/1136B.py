import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0 
ans += 1 # +1 throw away at k
ans += n # n pickups 
ans += n # n throwaways

# walk to each hole
ans += min(k - 1 + n - 1, n - k + n - 1)
print ans