# https://www.geeksforgeeks.org/count-integral-points-inside-a-triangle/


def boundary_points(a, b):
    dx = abs(a[0] - b[0])  # x2 - x1
    dy = abs(a[1] - b[1])  # y2 - y1
  
    # Count lattice points on the line segment (a, b)
    if dx == 0:
       return dy
    if dy == 0:
       return dx
      
    while dy:
          dx, dy = dy, dx % dy
    return dx 
      
    """(or) 
    from math import gcd
    gcd(abs(a[0] - b[0]), abs(a[1] - b[1]))
    """
def area(p, q, r):  
    # area of a rectangle
    return abs(p[0]*(q[1]-r[1]) + q[0]*(r[1]-p[1]) + r[0]*(p[1]-q[1])) / 2
      
def count_lattice_points(p, q, r):
    B = boundary_points(p, q) + boundary_points(q, r) + boundary_points(r, p)
    A = area(p, q, r)
    return int(A - B/2 + 1)

p = (0, 0)
q = (0, 5)
r = (5, 0)
print(count_lattice_points(p, q, r)) 
# 6
