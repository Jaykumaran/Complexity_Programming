# https://www.geeksforgeeks.org/check-whether-triangle-valid-not-sides-given/
"""

 A triangle is valid if sum of its two sides is greater than the third side. If three sides are a, b and c, then three conditions should be met. 

(a + b) > c
(a + c) > b
(b + c) > a 
"""

def valid_triangle(a, b, c):
    if (a + b > c) or (a + c > b) or (b + c > a):
       return True
    else:
       return False

a = 7
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid") 
else:
    print("Invalid")
