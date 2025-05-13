# https://www.geeksforgeeks.org/program-find-area-circular-segment/

"""
Formula used:
        Area = (π * a * a) / 2
    where:
        a = side length of the square

    Explanation:
    - The area of a circle is: Area = π * r^2
    - For a circle inscribed in a square, the diameter = side of the square (a)
    - Therefore, radius r = a / 2

    So:
        Area = π * (a / 2)^2
             = π * (a^2 / 4)

    However, if the circle is **circumscribed** about the square (i.e., the square fits inside 
    the circle), then:
    - The diagonal of the square is the diameter of the circle
    - Diagonal = √2 * a
    - Radius = (√2 * a) / 2

    Therefore:
        Area = π * [(√2 * a) / 2]^2
             = π * (2 * a^2) / 4
             = (π * a^2) / 2
"""

PI = 3.14159265

def areacircumscribed(a):
    return (a * a * (PI / 2))

a = 6
print(" Area of an circumscribed circle is :",
        round(areacircumscribed(a), 2))
        
