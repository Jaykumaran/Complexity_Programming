# https://www.geeksforgeeks.org/c-program-find-area-triangle/

# Given the sides of a triangle, the task is to find the area of this triangle.

"""
    Heron's Formula:
        Area = √(s * (s - a) * (s - b) * (s - c))
    where:
        s = (a + b + c) / 2 # semi Perimeter
        """

def findArea(a, b, c):

    # Check whether its a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
       return 0 # Invalid triangle

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

  
# Initialize first side of triangle  
a = 3.0
# Initialize second side of triangle  
b = 4.0
# Initialize Third side of triangle  
c = 5.0
findArea(a,b,c)  

# 6.0
