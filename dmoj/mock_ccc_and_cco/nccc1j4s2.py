import sys
input = sys.stdin.readline

n = int(input())
g = []

def p(a):
    res = []
    for x in a:
        try:
            res.append(int(x))
        except:
            res.append(ord(x) - 55)
    return res
for i in range(n):
    g.append(list(p(list(input().strip()))))

if all(len(set(g[x])) == n for x in range(n)) and all(len(set([x[0] for x in g])) == n for x in range(n)):
    if sorted(g[0]) != g[0] or sorted([x[0] for x in g]) != [x[0] for x in g]:
        print "Latin"
    else:
        print "Reduced"
else:
    print "No"
