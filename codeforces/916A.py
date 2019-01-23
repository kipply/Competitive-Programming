import sys
input = sys.stdin.readline

x = int(input())

ans = 0

hh, mm = map(int, input().split())

time = (mm + hh * 60) % (24 * 60)

while "7" not in str(time % 60) and "7" not in str(time / 60): 
  time -= x
  time = (time + (24 * 60)) % (24 * 60)
  ans += 1


print ans