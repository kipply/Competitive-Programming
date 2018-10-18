a = int(input())
b = int(input())
c = []
for i in range(b):
    d = int(input())
    c.append(d)
c = sorted(c)
ans = 0
temp = 0
for i in range(b):
    temp += c[i]
    if temp > a:
        break
    ans += 1

print(ans)
