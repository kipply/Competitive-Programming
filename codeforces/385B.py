import sys, math, re
input = sys.stdin.readline

s = input().strip()

found = [(m.start(), m.end()) for m in re.finditer('bear', s)]
# print len(found), len(s)
if found: 
  ans = (found[0][0] + 1)*(len(s) - found[0][1] + 1)
  for i, bear in enumerate(found[1:]): 
    start = bear[0]
    end = bear[1]
    ans += min(start - found[i][0], start + 1)*(len(s) - end + 1)
    # print start, end, ans
else: 
  ans = 0 
print ans