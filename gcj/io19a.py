import sys
input = sys.stdin.readline

t = int(input())

def desirable(arr): 
  for i in range(1, len(arr) - 1): 
    if any(arr[j] < arr[i] for j in range(i)) and any(arr[j] < arr[i] for j in range(i + 1, len(arr))): 
      return True
    elif any(arr[j] > arr[i] for j in range(i)) and any(arr[j] > arr[i] for j in range(i + 1, len(arr))): 
      return True
  return False 

for C in range(1, t + 1): 
  k = int(input())
  m = list(map(int, input().split()))

  ans = 0 
  curr = [0, 3] # exclusive
  while True:
    # print curr
    if curr[1] == k: 
      break
    if desirable(m[curr[0]:curr[1]]) and desirable(m[curr[1] - 1:]): 
      ans += 1
      if curr[1] + 2 > k: 
        break
      curr[0] = curr[1] - 1
      curr[1] = curr[0] + 3
    else: 
      curr[1] += 1


  print "Case #" + str(C) + ": " + str(ans)
