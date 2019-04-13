import sys
import math
input = sys.stdin.readline 

n, b = map(int, input().split())
factors = set() 
def pf(n): 
  while not n % 2: 
    factors.add(2)
    n /= 2 
  for i in range(3, int(n ** 0.5 + 1), 2): 
    while not n % i: 
      factors.add(i)
      n /= i
  if n > 2: 
    factors.add(n)
pf(b)


count = n
j = b
for i in factors: 
  p = 0 
  while not j % i: 
    p += 1 
    j /= i

  # c should be the max power of p in n!
  c = 0 
  k = n 
  while k / i > 0: 
    c += k / i 
    k /= i
  count = min(count, c / p)
print count

# print "Now deffing"
# for i, x in enumerate(num_w_base(math.factorial(n), b)[::-1]): 
#   if x: 
#     definitely_correct = i
#     break
# print (definitely_correct, "Def")