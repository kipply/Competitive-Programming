plain = raw_input()
cipher = raw_input()

message = raw_input()
ans = ""
for l in list(message):
    try:
        ans += plain[cipher.index(l)]
    except:
        ans += '.'
print ans
