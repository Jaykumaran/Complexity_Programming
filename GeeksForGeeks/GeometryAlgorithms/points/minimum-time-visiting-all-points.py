# https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=problem-list-v2&envId=geometry

"""
Move horizontally (1 unit),

Move vertically (1 unit),

Or move diagonally (1 unit both in x and y at the same time — 1 second).

To go from point A to B in the minimum time, always move diagonally as much as possible, and then straight (horizontal/vertical) if needed.
"""

# Move diagonally, so that the direction that takes more time is the req time to move between those two points
# Similarly accumulate the time taken for other points
def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(1, len(points)): # start with 1, so that 1->0, 2->1, ...
        dx = abs(points[i][0] - points[i-1][0])
        dy = abs(points[i][1] - points[i-1][0])
        time += max(dx, dy)
    return time


points = [[1, 1], [3, 4], [-1, 0]]
print(minTimeToVisitAllPoints(points))

# 7
