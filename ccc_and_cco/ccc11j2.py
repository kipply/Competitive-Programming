h = int(input())
m = int(input())

ans = "The balloon does not touch ground in the given time."

for t in range(1, m + 1):
    if -6 * (t ** 4) + h * (t ** 3) + 2 * (t ** 2) + t < 1:
        ans = "The balloon first touches ground at hour: \n" + str(t)
        break
print ans
