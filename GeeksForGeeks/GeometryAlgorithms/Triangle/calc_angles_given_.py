# https://www.geeksforgeeks.org/find-angles-given-triangle/
# Find all angles of a given triangle


"""
Given coordinates of all three vertices of the triangle in the 2D plane, the task is to find all three angles.

c^2 = a^2 + b^2 - 2(a)(b)(cos beta)
After re-arranging 
 

beta = acos( ( a^2 + b^2 - c^2 ) / (2ab) )
In trigonometry, the law of cosines (also known as the cosine formula or cosine rule) relates the lengths of the sides of a triangle to the cosine of one of its angles.
 

First, calculate the length of all the sides. 
Then apply above formula to get all angles in 
radian. Then convert angles from radian into 
degrees.
"""

import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def angle_from_sides(a, b, c):
    # Returns angle (in deg) opposite side 'a'
    return math.degrees(math.acos((b**2+c**2-a**2) / (2 * b * c)))

def triangle_angles(A, B, C):
    # Calc side lengths
    a = distance(B, C) # side opp to A
    b = distance(A, C) # side opp to B
    c = distance(A, B) # side opposite C

    # Caculate angles using Law of Cosines
    angle_A = angle_from_sides(a, b, c)
    angle_B = angle_from_sides(b, a, c)
    angle_C = angle_from_sides(c, a, b)
    return int(angle_A), int(angle_B), int(angle_C)
  
A = (0, 0)
B = (0, 1)
C = (1, 0)

angles = triangle_angles(A, B, C)
