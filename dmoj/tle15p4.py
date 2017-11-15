n = int(raw_input())
mod = 1000000013

if n < 4:
  print(1)
else:
  ans = pow(2, n - 2, mod)
  if n % 8 == 2 or n % 8 == 6:
    ans = pow(2, n - 2, mod)
  elif n % 8 == 1 or n % 8 == 7:
    ans = (ans + pow(2, (n - 1) // 2 - 1, mod))
  elif n % 8 == 3 or n % 8 == 5:
    ans = (ans - pow(2, (n - 1) // 2 - 1, mod))
  elif n % 8 == 0:
    ans = (ans + pow(2, n // 2 - 1, mod))
  elif n % 8 == 4:
    ans = (ans - pow(2, n // 2 - 1, mod))
  print(ans % mod)
