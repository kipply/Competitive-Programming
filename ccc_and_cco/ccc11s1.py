a = int(input())
s = ""
for i in range(a):
    s += input()
s = s.lower()
ts = s.count('t')
ss = s.count('s')
if ss >= ts:
    print("French")
else:
    print("English")
