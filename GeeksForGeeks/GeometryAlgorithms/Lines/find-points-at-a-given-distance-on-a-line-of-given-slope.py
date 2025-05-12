# https://www.geeksforgeeks.org/find-points-at-a-given-distance-on-a-line-of-given-slope/


# There is two points possible from a given point with same distance and slope

def points_on_line_given_slope(x0, y0, L, M):

    magnitude = math.sqrt(1 + M**2)

    # Unit direction vector scaled by a distance L
    dx = L / magnitude
    dy = M * L / magnitude

    # Calc the two points
    point1 = (x0 + dx, y0+dy)
    point2 = (x0 - dx, y0-dy)

    return point1, point2


"""
In [24]: p1, p2 = points_on_line_given_slope(2, 1, math.sqrt(2), 1)

In [25]: p1
Out[25]: (3.0, 2.0)

In [26]: p2
Out[26]: (1.0, 0.0)


"""
"""
Moving L units along the line of slope M.
  Steps:
    1. Represent the slope M as a direction vector (1, M).
    2. Normalize this vector to get a unit direction vector.
       That is, divide by its magnitude sqrt(1 + M^2).
    3. Scale this unit vector by the distance L to get the actual displacement (dx, dy).
    4. Add and subtract this displacement from the original point to get the two target points.

|d⃗| = √(1 + M²)

Unit direction vector:
d̂ = (1 / √(1 + M²), M / √(1 + M²))

Scale unit vector by distance L:

The vector of length L in the direction of the line is:
v⃗ = L ⋅ d̂ = (L / √(1 + M²), L⋅M / √(1 + M²))

Find two points at distance L:

Add and subtract this vector from the original point:

Point1 = (x₀ + L / √(1 + M²), y₀ + L⋅M / √(1 + M²))
Point2 = (x₀ - L / √(1 + M²), y₀ - L⋅M / √(1 + M²))
"""
