import sys
input = sys.stdin.readline
#this is kind of dp?
n, m = map(int, input().split())
adj = [[] for x in range(n + 1)]
goes_to = [0 for x in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    goes_to[y] += 1

r = [0 for x in range(n + 1)]


def f(i):
      r[i] = 1
      for x in adj[i]:
        'if not r[x]: f(x)


f(1)
for i in range(1, n + 1):
    if not r[i]:
        for x in adj[i]:
            goes_to[x] -= 1

idk_what_to_le_call = [0 for x in range(n + 1)]
q = [1]
s = []
while q:
  t = q.pop(0)
  s.append(t)
  for x in adj[t]:
    goes_to[x] -= 1
    if goes_to[x] == 0:
      q.append(x)
p = 0

for i in range(len(s)):
  x = s[i]
  if i == 0:
    idk_what_to_le_call[x] = 1
  for c in adj[x]:
    if idk_what_to_le_call[c] + idk_what_to_le_call[x] >= 1000000000:
      p = 1
    idk_what_to_le_call[c] += idk_what_to_le_call[x]
if p:
    # Sketchy method of getting the last 9 digits
  print(str(idk_what_to_le_call[2])[len(str(idk_what_to_le_call[2])) - 9:])
else:
  print(idk_what_to_le_call[2])
