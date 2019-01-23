n, k = map(int, raw_input().split())
a = 0
b = 1

while b < k and b < n:
    b += b
    a += 1
print a + (n - b + k - 1) / k
