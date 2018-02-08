import sys
input = sys.stdin.readline

dordor = input().strip()
dordor = dordor.replace("=", "==")
print eval(dordor)