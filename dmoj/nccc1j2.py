s = raw_input()

def palindrome_substrings(string):
    return (i for i in (string[i:j+1] for i in range(len(string)) for j in range(i, len(string))) if i == i[::-1])

ans = "Odd"
for p in list(palindrome_substrings(s)):
    if len(p) % 2 == 0:
        ans = "Even"
        break
print ans