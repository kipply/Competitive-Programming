import sys
input = sys.stdin.readline 

n, k_1, k_2 = map(int, input().split())
k = k_2 + k_1
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diffs = [abs(a[i] - b[i]) for i in range(n)]
diffs.sort(reverse=True)


# print diffs, k
for i in range(n - 1): 
  if diffs[i] > diffs[i + 1] and k:

    x = diffs[i] - diffs[i + 1] 
    if x * (i + 1) > k: 
      y = k / (i + 1)
      for j in range(i + 1): 
        diffs[j] -= y
        k -= y
      for j in range(k): 
        diffs[j] -= 1
        k -= 1
    else: 
      for j in range(i + 1): 
        diffs[j] -= x
        k -= x 


if k and diffs[0]: 
  while k: 
    if not sum(diffs): break
    for i in range(n):
      if not k: break
      diffs[i] -= 1 
      k -= 1

if k % 2: 
  diffs[0] = 1

ans = sum([x**2 for x in diffs])
print ans