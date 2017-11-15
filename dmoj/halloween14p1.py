n = int(input())
k = int(input())
print(k - n % k) if n < k else print(min(k - n % k, n % k))
