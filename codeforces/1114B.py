import sys
input = sys.stdin.readline 

n, m, k = map(int, input().split())

a = list(map(int, input().split()))
s = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1])][::-1][:m * k]
s.sort()
ans = sum(a[s[i]] for i in range(m * k))
print ans
ans = []
for i in range(m - 1, k*m - 1, m): 
  ans.append(str(s[i] + 1))

print " ".join(ans)