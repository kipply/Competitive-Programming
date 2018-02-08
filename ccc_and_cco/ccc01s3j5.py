cactus = [[0 for x in range(26)] for x in range(26)]

while True:
  t = list(raw_input())
  if t[0] == "*":
    break
  cactus[ord(t[0]) - 65][ord(t[1]) - 65] = 1
  cactus[ord(t[1]) - 65][ord(t[0]) - 65] = 1

ans = 0

def dfs(node):
  global f
  global v
  if node == 1:
    f = 1
    return
  v[node] = 1
  for i in range(26):
    if not v[i] and cactus[node][i]:
      v[i] = 1
      dfs(i)
      v[i] = 0

for i in range(26):
  for j in range(i + 1, 26):
    v = [0] * 26
    if cactus[i][j]:
      cactus[i][j] = cactus[j][i] = 0
      f = 0
      dfs(0)
      if not f:
        ans += 1
        print(chr(i + 65) + chr(j + 65))
      cactus[i][j] = cactus[j][i] = 1
print("There are " + str(ans) +  " disconnecting roads.")
