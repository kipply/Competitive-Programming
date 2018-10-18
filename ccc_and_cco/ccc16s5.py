# Basically, powers of two do interesting things, use xors and mod to wrap
import sys
n = sys.stdin.readline().split()
t = int(n[1])
n = int(n[0])
dordor = map(int, sys.stdin.readline().strip()) # Dordor is the best variable name
covfefe = 1
for i in range(45, -1, -1):
    while t >= covfefe << i:
        covfefetemp = covfefe << i
        angery = [0] * n
        for k in range(n):
            angery[(k - covfefetemp) % n] ^= dordor[k] # ^ is Exclusive Or.
            angery[(k + covfefetemp) % n] ^= dordor[k]
        dordor = angery
        t -= covfefetemp
sys.stdout.write(''.join(str(x) for x in dordor))
