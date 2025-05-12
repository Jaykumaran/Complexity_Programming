# https://www.geeksforgeeks.org/program-calculate-area-circumcircle-equilateral-triangle/

# Program to calculate area of Circumcircle of an Equilateral Triangle

"""
All three sides of equilateral triangle are of equal length and all three interior angles are 60 degrees.
Properties of a Circumcircle are as follows: 
 

- The center of the circumcircle is the point where the medians of the equilateral triangle intersect.
- Circumscribed circle of an equilateral triangle is made through the three vertices of an equilateral triangle.
- The radius of a circumcircle of an equilateral triangle is equal to (a / ?3), where ‘a’ is the length of the side of equilateral triangle.

area = (PI * a**2) / 3
"""
PI = 3.14159265

def area_circumscribed(a):
    return (a * a * (PI / 3))

a = 6.0
area_circumscribed(a)
# 37.699111800000004
