"""
Input : P(3, 2)
        Q(2, 6)
Output : 4x + 1y = 14

Input : P(0, 1)
        Q(2, 4)
Output : 3x + -2y = -2


Let the given two points be P(x1, y1) and Q(x2, y2). Now, we find the equation of line formed by these points.
Any line can be represented as, 
ax + by = c 
Let the two points satisfy the given line. So, we have, 
ax1 + by1 = c 
ax2 + by2 = c 
a = y2 - y1  # Positive
b = x1 - x2  # Neg or Pos
c = ax1 + by1
"""
def lineFromPoints(P, Q):
    a  = Q[1] - P[1]
    b  = P[0] - Q[0]
    c = (a*(P[0])) + (b * (P[1]))

    if (b < 0):
       eqn = f"{a}x - {b}y = {c}"
       print(eqn)
    else:
       eqn = f"{a}x + {b}y = {c}"
       print(eqn)


P = [3, 2]
Q = [2, 6]
lineFromPoints(P, Q)

# 4x + 1y = 14

# https://www.geeksforgeeks.org/program-find-line-passing-2-points/




