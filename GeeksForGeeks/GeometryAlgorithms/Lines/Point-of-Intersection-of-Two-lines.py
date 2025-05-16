"""
Line 1: a1*x + b1*y = c1  
Line 2: a2*x + b2*y = c2
"""

def find_intersection(a1, b1, c1, a2, b2, c2):

    # Calc det
    determinant = a1 * b2 - a2 * b1 

    if determinant == 0:
       return "The lines are parallel or coincide (no unique solution)"

    # Cramer rule
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)

a1, b1, c1 = 1, -1, 0   # Line 1: x - y = 0
a2, b2, c2 = 1, 1, 4    # Line 2: x + y = 4

intersection = find_intersection(a1, b1, c1, a2, b2, c2)


# Steps:
       Step 1: Compute the determinant of the coefficient matrix:
        Det = | a1  b1 |
              | a2  b2 | = (a1 * b2) - (a2 * b1)

    Step 2: If Det ≠ 0, the system has a unique solution.

    Compute x and y using:

        x = | c1  b1 | / Det = (c1 * b2 - c2 * b1) / Det
            | c2  b2 |

        y = | a1  c1 | / Det = (a1 * c2 - a2 * c1) / Det
            | a2  c2 |
      Matrix notation:

      x = det([[c1, b1],
               [c2, b2]]) / Det

      y = det([[a1, c1],
               [a2, c2]]) / Det

