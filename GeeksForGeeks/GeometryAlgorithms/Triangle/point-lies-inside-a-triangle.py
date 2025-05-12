# https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/

"""
Let the coordinates of the three corners be (x1, y1), (x2, y2), and (x3, y3). And coordinates of the given point P be (x, y)

1. Calculate the area of the given triangle, i.e., the area of the triangle ABC in the above diagram. 
Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2 
2. Calculate the area of the triangle PAB. We can use the same formula for this. Let this area be A1. 
3. Calculate the area of the triangle PBC. Let this area be A2. 
4. Calculate the area of the triangle PAC. Let this area be A3. 
5. If P lies inside the triangle, then A1 + A2 + A3 must be equal to A. 
"""

# Shoelace formula for calc. area of triangle given three points
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3-y1) + x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):

  # Cacl area of ABC
  A = area(x1, y1, x2, y2, x3, y3)

  # PBC
  A1 = area(x, y, x2, y2, x3, y3)

  # PAC
  A2 = area(x1, y1, x, y, x3, y3)

  # PAB
  A3 = area(x1, y1, x2, y2, x, y)

  if (A == A1 + A2 + A3):
      return True  
  else:
      return False

valid = isInside(0, 0, 20, 0, 10, 30, 10, 15)
print(valid)  # False


