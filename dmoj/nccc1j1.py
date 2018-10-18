n = int(input())
while True:
    n += 1
    try:
        str(n).index('0')
    except:
        print n
        break
