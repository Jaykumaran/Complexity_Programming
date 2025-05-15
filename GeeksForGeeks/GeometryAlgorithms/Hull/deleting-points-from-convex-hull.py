# Finding the Convex Hull of a set of 2D points, and updating it when a point is removed.


# https://youtu.be/8foCOARqH8A?feature=shared

# Andrew’s monotone chain algorithm which is simple version of Graham scan

# tell us the turn direction 
def cross(o, a, b):
    """
    2D Cross Product to check orientation:
    (x2 - x1)*(y3 - y2) - (y2 - y1)*(x3 - x2)
    Returns:
        >0 for counter-clockwise
        <0 for clockwise, remove the middle point
        =0 for collinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
  
    return lower[:-1] + upper[:-1]  # remove the last point from both lower and upper because it's duplicated (start and end point are the same)



# Initial set
points = [(-2, 8), (-1, 2), (0, 1), (1, 0), (-3, 0), (-1, -9), (2, -6), (3, 0), (5, 3), (2, 5)]

# Compute initial convex hull
hull = convex_hull(points)
print("Initial Convex Hull:", hull)

# Remove a point
remove_point = (-2, 8)

if remove_point in hull:
   points.remove(remove_point)
   hull = convex_hull(points)

print("Final Convex Hull:", hull)


# Initial Convex Hull: [(-3, 0), (-1, -9), (2, -6), (5, 3), (-2, 8)]
# Final Convex Hull: [(-3, 0), (-1, -9), (2, -6), (5, 3), (2, 5)]




      
