import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

cuteness = [0] + list(map(int, input().split()))

queries = [] 

for i in range(Q): 
  queries.append(list(map(int, input().split())))

queries.sort(key=lambda x: x[2])

ans = [0 for _ in range(max(cuteness) + 1)]
for i in range(N): 
  cuteness[i + 1] += cuteness[i]

for l, r, k in query: 
  s = cuteness[r] - cuteness[l]
print queries