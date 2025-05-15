# https://www.geeksforgeeks.org/check-given-four-points-form-square/

"""
**All sides equal.
**Diagonals equal.
** All angles are 90° (via dot product).
If the dot product of two vectors(coords) is 0, it means the vectors are perpendicular.
Eg: in <ABC, AB and BC are perp if their slope is 0
"""


def is_square(p1, p2, p3, p4):
  def dist2(a, b):
      return (a[0]-b[0])**2 + (a[1]-b[1])**2
  def dot(a, b, c):
      ab = (b[0]-a[0] , b[1]-a[1])
      bc = (c[0]-b[0], c[1]-b[1])
      return ab[0]*bc[0] + ab[1]*bc[1]

  pts = [p1, p2, p3, p4]

  orders = [
    (pts[0], pts[1], pts[2], pts[3]),
    (pts[0], pts[2], pts[3], pts[1]),
    (pts[0], pts[3], pts[1], pts[2])
  ]
      # fixed starting point
      # try one possible order: a is fixed, then b, c, d go around it
      # Cycles through 3 different configurations to cover all possible square orientations starting at `a`
  for a, b, c, d in orders:  
    if dist2(a, b) == dist2(b, c) == dist2(c, d) == dist2(d, a) > 0 \
        and dist2(a, c) == dist2(b, d) \
        and dot(a, b, c) == 0:
            # **All sides equal.
            # **Diagonals equal.
            # **All angles are 90° (via dot product).
            return True
  return False

print(is_square([20, 10], [10, 20], [20, 20], [10, 10]))  # True
print(is_square([20, 20], [10, 20], [20, 20], [10, 10]))  # False
