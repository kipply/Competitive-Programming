import sys
input = sys.stdin.readline
n, m = map(int, input().split())
food = [[] for x in range(n + 1)]
sys.setrecursionlimit(999999999)
for i in range(m):
  r = map(int, input().split())
  for x in r[2:]:
    food[r[0]].append(x)

ing = [0] + list(map(int, input().split()))

need = food[1]

def make(f):
  global ing
  c = 1
  if food[f]:
    for i in food[f]:
      make(i)
    if c:
      m = 1 << 35
      for i in food[f]:
        try:
          if ing[i] < 1:
            return
        except:
          return
        if ing[i] < m:
          m = ing[i]
      for i in food[f]:
        ing[i] -= m
      ing[f] += m

make(1)
print(ing[1])
