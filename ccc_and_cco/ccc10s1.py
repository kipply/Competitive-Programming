import sys
from operator import itemgetter
input = sys.stdin.readline

n = int(input())
cuteness = [] 
for i in range(n):
  honestly_having_strings_and_integers_on_the_same_line_is_weird = input().split()
  name = honestly_having_strings_and_integers_on_the_same_line_is_weird[0]
  r, s, d = map(int, honestly_having_strings_and_integers_on_the_same_line_is_weird[1:])

  cuteness.append((2 * r + 3 * s + d, name))

cuteness.sort(key=lambda x: (-x[0], x[1]))

if n >= 2: 
  print cuteness[0][1]
  print cuteness[1][1]
if n == 1: 
  print cuteness[0][1]
