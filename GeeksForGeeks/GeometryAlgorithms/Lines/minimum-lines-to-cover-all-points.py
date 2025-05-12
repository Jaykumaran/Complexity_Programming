# https://www.geeksforgeeks.org/minimum-lines-cover-points/
"""
Given N points and a fixed point (x0, y0), find the minimum number of straight lines that:

- All must pass through (x0, y0).

- Together must cover all N points.
"""

# If points lie in a collinear they have same slope and we just need a single line
# Consider for the unique slopes so that we can cater that many lines to cover all points
# The expectation wasn't to have a closed area

def min_lines(points, x0, y0):
    slopes = set() # unique
    for x,y in points:
        # m = dy/dx
        dy = y - y0
        dx = x - x0
        if dx == 0: # vertical , same x point
           slope = 'inf'
        else:
            slope = dy / dx
        slopes.add(slope)
    return len(slopes) # Number of unique slopes = number of lines min req to toouch upon all points
      
points = [(-1, 3), (4, 3), (2, 1), (-1, -2), (3, -3)]
x0, y0 = 1, 0
print(min_lines(points, x0, y0))  
# 2
