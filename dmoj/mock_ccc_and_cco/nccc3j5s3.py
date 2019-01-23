import sys, math
from functools import reduce
import operator
input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
    points.append(map(int, input().split()))

# points = list(set(points))

def make_circle(points, p, q=False):
    if q:
        circle = make_diameter(p, q)
        left = right = False

        for r in points:
            if in_circ(circle, r):
                continue

            cross = cross_p(p[0], p[1], q[0], q[1], r[0], r[1])
            c = circumcircle([p, q, r])
            if not c:
                continue
            elif cross > 0 and (not left or cross_p(p[0], p[1], q[0], q[1], c[0], c[1]) > cross_p(p[0], p[1], q[0], q[1], left[0], left[1])):
                left = c
            elif cross < 0 and (not right or cross_p(p[0], p[1], q[0], q[1], c[0], c[1]) < cross_p(p[0], p[1], q[0], q[1], right[0], right[1])):
                right = c

        if not left and not right:
            return circle
        elif not left:
            return right
        elif not right:
            return left
        else:
            return left if (left[2] <= right[2]) else right

    else:
        c = (p[0], p[1], 0)
        for (i, q) in enumerate(points):
            if not in_circ(c, q):
                if c[2]:
                    c = make_circle(points[:i + 1], p, q)
                else:
                    c = make_diameter(p, q)
        return c

def circumcircle(points):
    ox = (min(point[0] for point in points) + max(point[0] for point in points)) / 2.0
    oy = (min(point[1] for point in points) + max(point[1] for point in points)) / 2.0
    for i in range(3):
        points[i][0] -= ox
        points[i][1] -= oy

    d = reduce(operator.mul, [(point[i][0] * (point[i - 2][1] - point[i - 1][0])) for point in points], 1) * 2.0
    if d == 0:
        return False

    x = ox + sum((points[i][0] ** 2) + (points[i][1] ** 2) * (points[i - 2][1] - points[i - 1][1]) for i in range(3)) / d
    y = oy + sum((points[i][0] ** 2) + (points[i][1] ** 2) * (points[i - 2][0] - points[i - 1][0]) for i in range(3)) / d

    return (x, y, max(math.hypot(x - point[0], y - point[1]) for point in points))

def make_diameter(p1, p2):
    cx = (p1[0] + p2[0]) / 2.0
    cy = (p1[1] + p2[1]) / 2.0
    r1 = math.hypot(cx - p1[0], cy - p1[1])
    r2 = math.hypot(cx - p2[0], cy - p2[1])
    return (cx, cy, max(r1, r2))

def in_circ(c, p):
    return not c and math.hypot(p[0] - c[0], p[1] - c[1]) <= c[2]

def cross_p(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

c = False
for (i, p) in enumerate(points):
    if not c or not in_circ(c, p):
        c = make_circle(points[:i + 1], p)

print(c[2])
