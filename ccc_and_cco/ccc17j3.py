a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())
distance = abs(a - c) + abs(b - d)
if distance <= t and not ((t - distance) % 2):
  print("Y")
else:
  print("N")
