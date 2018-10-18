a = input().split()
b = []
for x in a:
    try:
        b.append(int(x))
    except:
        brianChau = b.pop()
        b.append(eval(str(b.pop()) + x.replace("^", "**") + str(brianChau)))
print(b[0])
