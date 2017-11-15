# this is the preprocessor!

import struct
import os
interval = 133000
x = 1
val = 1
ans = ""
f = open('boop.txt', 'wb')
d = 0
while x < (2 ** 32 - 5):
    x += 1
    val = (x * val) % (2 ** 32 - 5)
    if not x % interval:
        a = val >> 16
        b = val & 65535
        a = unichr(int(a) + 100000)
        b = unichr(int(b) + 100000)
        f.write((a + b).encode('utf-8'))
print(d)
