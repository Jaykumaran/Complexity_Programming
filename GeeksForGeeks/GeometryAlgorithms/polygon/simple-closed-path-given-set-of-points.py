# https://www.geeksforgeeks.org/find-simple-closed-path-for-a-given-set-of-points/

"""
1. Find the bottom-most point by comparing y coordinate of all points. If there are two points with same y value, then the point with smaller x coordinate value is considered. Put the bottom-most point at first position.

2. Consider the remaining n-1 points and sort them by polar angle in counterclockwise order around points[0]. If polar angle of two points is same, then put the nearest point first.

3. Traversing the sorted array (sorted in increasing order of angle) yields simple closed path. 
"""

import math

def bottom_point(points):
    # Find the bottom point (lowest y, if equal lowest x), anchor
    return min(points, key = lambda p: (p[1], p[0]))


def polar_angle_sort(points):
    p0 = bottom_point(points) # lowest point
    def angle_and_distance(p):
        # calc polar angle # atan2(y, x)
        # This differencing ensures: anchor point --> point
        angle = math.atan2(p[1] - p0[1], p[0] - p0[0]) # polar angle from anchor to a given point
        dist = (p[0] - p0[0])**2 + (p[1] - p0[1])**2
        return (angle, dist)

    sorted_points = sorted(points, key = angle_and_distance)
    return [p0] + [p for p in sorted_points if p!=p0]  # ensures p0 at start

def simple_closed_path(points):
    return polar_angle_sort(points)

points = [(0, 3), (1, 1), (2, 2), (4, 4),
          (0, 0), (1, 2), (3, 1), (3, 3)]

path = simple_closed_path(points)

print("Simple Closed Path:")
for p in path:
    print(p)


# Simple Closed Path:
# (0, 0)
# (3, 1)
# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)
# (1, 2)
# (0, 3)



        

