a = input()
b = input()
c = list("abcdefghijklmnopqrstuvwxyz")
f = False
for l in c:
    if a.count(l) < b.count(l):
        print ("N")
        f = True
        break
if not(f):
    print ("A")
