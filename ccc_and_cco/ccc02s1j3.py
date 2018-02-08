import sys
input = sys.stdin.readline

pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())

count = 0
mini = 1 << 30

for a in range(total // pink + 1):
    for b in range(total // green + 1):
        for c in range(total // red + 1):
            for d in range(total // orange + 1):
                if ((a * pink) + (b * green) + (c * red) + (d * orange) == total):
                    print("# of PINK is", a, "# of GREEN is", b, "# of RED is", c, "# of ORANGE is", d)
                    count += 1
                    if sum([a, b, c, d]) < mini:
                        mini = sum([a, b, c, d])
print("Total combinations is " + str(count) + ".")
print("Minimum number of tickets to print is " + str(mini) + ".")