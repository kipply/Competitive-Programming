# Who needs recursion when you're in python? 
from itertools import permutations
import sys
a = raw_input()
a = [x for x in permutations(a)]
a.sort()
for i in a:
  for j in i:
    sys.stdout.write(j)
  print("")
