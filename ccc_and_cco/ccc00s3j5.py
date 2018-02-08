import sys, re
from collections import deque
input = sys.stdin.readline

n = int(input())
cactus = {}
for i in range(n):
  url = input().strip()
  cactus[url] = []
  while True:
    temp = input().strip()
    links = re.findall(r'HREF="(.*?)"', temp)
    for l in links:
      cactus[url].append(l)
      print("Link from " + url + " to " + l)
    if "</HTML>" in temp:
      break
while True:
  a = input().strip()

  if a == "The End":
    break
  b = input().strip()
  q = [a]
  f = 0
  v = {}
  while q:
    link = q.pop(0)
    if link == b:
      f = 1
      break
    v[link] = 1
    for dest in cactus[link]:
      if dest not in v:
        q.append(dest)
  if f:
    print("Can surf from " + a + " to " + b + ".")
  else:
    print("Can't surf from " + a + " to " + b + ".")
