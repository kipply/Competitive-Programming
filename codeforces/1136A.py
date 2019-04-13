import sys
input = sys.stdin.readline

n = int(input())
chapters = [map(int, input().split()) for _ in range(n)]
k = int(input())

ans = n 
for chapter in chapters: 
  if k > chapter[1]:
    ans -= 1

print ans
