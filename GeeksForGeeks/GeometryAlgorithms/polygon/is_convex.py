"""
Check if a Polygon is Convex:
Question: Given the vertices of a simple polygon in order, determine if the polygon is convex.

If > 0 → Counterclockwise turn (left turn)

If < 0 → Clockwise turn (right turn)

If = 0 → Points are collinear (no turn)

**Convexity Rule**:

- If all cross products (turns) have the same sign (all left turns or all right turns), then the polygon is convex.
- If the sign changes (some left, some right), then the polygon is concave.

"""

def is_convex(polygon):
    def cross(a, b, c):
        """
         Cross Product Formula (Orientation of points A, B, C):
        (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        """
        return (b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0])

    n = len(polygon)
    sign = None
    for i in range(n):
        c = cross(polygon[i], polygon[(i+1)%n], polygon[(i+2)%n])
        if c != 0:
           if sign is None:
              sign = c > 0
           elif sign != (c > 0):  # non-convex if direction changes
                return False
    return True # If all turns are consistent, return True.

poly1 = [[0,0], [4,0], [4,4], [0,4]]        # Convex
poly2 = [[0,0], [4,0], [2,2], [4,4], [0,4]] # Not Convex

print(is_convex(poly1))  # True
print(is_convex(poly2))  # False
