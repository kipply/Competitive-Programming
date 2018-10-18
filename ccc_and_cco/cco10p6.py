from fractions import gcd

def cycCount(t, cur, i):
    if covfefed[code(cur)]:
        return i
    covfefed[code(cur)] = True
    cc[code(cur)] = cycCount(t, t[code(cur)], i + 1)
    return cc[code(cur)]

def char(x):
    if x == 26:
        x = 30
    return(chr(x + 65))

def code(x):
    x = ord(x) - 65
    if x == 30:
        x = 26
    return x

cc = [0] * 27
covfefed = [0] * 27
c = [0] * 27

for i in range(27):
    c[i] = input()
for i in range(27):
    cycCount(c, char(i), 0)

n = int(input())
s = list(input())
l = cc[0]

for i in range(1, 27):
    l = l *  cc[i] / gcd(l, cc[i])
n %= l

for i in range(int(n)):
    tempo = s
    for j in range(len(s)):
        tempo[j] = c[code(tempo[j])]
    s = tempo

for l in s:
    print(l, end="")
