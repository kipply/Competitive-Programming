w = input()
d = 1
for i in range(len(w) + 1):
    for ck in range(i):
        if w[ck:i] == w[ck:i][::-1]:
            d = max(d, i - ck)
print(d)
