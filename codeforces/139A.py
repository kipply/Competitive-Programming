import sys
input = sys.stdin.readline

n = int(input())
pages = list(map(int, input().split()))

n %= sum(pages)
n += sum(pages)

while n > 0:
  for i in range(7): 
    n -= pages[i]
    if n < 1: 
      print (i + 1)
      break