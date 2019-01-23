import sys
import itertools

input = sys.stdin.readline 

n = int(input()) 


def f(cactus, idx): 
  global ans
  if idx is 1: 
    for a in cactus: 
      if a and a <= 24: 
        ans.append(a)
        break
  else: 
    for i in range(len(cactus)): 
      for j in range(len(cactus)): 
        if i != j and cactus[i] and cactus[j]: 
          ti = cactus[i]
          tj = cactus[j]
          cactus[j] = False 

          cactus[i] += tj 
          f(cactus, idx - 1)

          cactus[i] = ti - tj
          f(cactus, idx - 1)

          cactus[i] = ti * tj
          f(cactus, idx - 1)

          cactus[i] = ti / float(tj) 
          if int(cactus[i]) == cactus[i]: 
            f(cactus, idx - 1)

          cactus[i] = ti 
          cactus[j] = tj 


for _ in range(n): 
  cards = [] 
  ans = []
  for i in range(4): 
    cards.append(int(input()))

  f(cards, 4)
  ans.sort()
  print(int(ans[-1]))