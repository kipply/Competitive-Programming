k, p, x = map(int, raw_input().split())
prev = 1 << 30
for i in range(1, max(k, p, x) + 2):
    num = (float(i) * x) + ((k * p) / float(i))
    if prev > num:
        prev = num
    else:
        print "{0:.3f}".format(prev)
        break
