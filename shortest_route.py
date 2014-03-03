from math import cos, sin, radians, acos
import itertools, re
from sys import argv

def two_three(point):
    a, b = map(radians, point)
    return (abs(cos(a))*cos(b), abs(cos(a))*sin(b), sin(a))

def get_angle(a, b):
    ab = sum(i*j for i, j in zip(a, b))
    return acos(ab)

points = []
f = open(argv[1], 'r')
for one in f:
    if one.strip():
        floats = re.findall(r"[-+]?\d+\.\d+", one)
        a, b = map(float, floats)
        points.append((a, b))
f.close()
points = map(two_three, points)

min_angle = None
ans = None
for one in itertools.permutations(range(1,9)):
    total_angle = 0
    one = (0,) + one + (9,)
    for i in range(len(one)-1):
        total_angle += get_angle(points[one[i]], points[one[i+1]])
    if min_angle is None or total_angle <= min_angle:
        min_angle = total_angle
        ans = one

for i in ans:
    print i + 1



