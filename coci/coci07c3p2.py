a = input()
for i in range(3 - (len(a) % 3)):
    a = "0" + a
b = ""
for i in range(0, len(a), 3):
    if a[i:i + 3] == "000":
        b = "0" + b
    elif a[i:i + 3] == "001":
        b = "1" + b
    elif a[i:i + 3] == "010":
        b = "2" + b
    elif a[i:i + 3] == "011":
        b = "3" + b
    elif a[i:i + 3] == "100":
        b = "4" + b
    elif a[i:i + 3] == "101":
        b = "5" + b
    elif a[i:i + 3] == "110":
        b = "6" + b
    else:
        b = "7" + b
print(b.strip("0")[::-1])
