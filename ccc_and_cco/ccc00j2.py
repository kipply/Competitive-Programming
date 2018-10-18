a = int(input())
b = int(input())
ans = 0
for i in range(a, b):
    flag = True
    if "2" in str(i) or "3" in str(i) or "4" in str(i) or "5" in str(i) or "7" in str(i):
        flag = False
    else:
        s = str(i)
        sr = list(str(i)[::-1])
        for i in range(0, len(sr)):
            if sr[i] == "6":
                sr[i] = "9"
            elif sr[i] == "9":
                sr[i] = "6"
        sr = "".join(sr)
        if s == sr:
            ans += 1
print(ans)
