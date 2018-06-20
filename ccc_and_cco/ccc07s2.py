import sys, operator
input = sys.stdin.readline

n = int(input())
boxes = []
for i in range(n):
    boxes.append(map(int, input().split()))
# sort by increasing product
boxes.sort(key=lambda x: reduce(operator.mul, x, 1))

m = int(input())
for i in range(m):
    dimensions = sorted(list(map(int, input().split())))
    ans = "Item does not fit."
    for box in boxes:
        box.sort()
        yay = True
        for j in range(3):
            if box[j] < dimensions[j]:
                yay = False
        if yay:
            ans = box[0] * box[1] * box[2]
            break
    print ans
