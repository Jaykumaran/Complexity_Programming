# https://www.geeksforgeeks.org/program-find-third-side-triangle-using-law-cosines/
"""
c^2 = a^2 + b^2 - 2*a*b*cos(c) 
OR
c = sqrt(a^2 + b^2 - 2*a*b*cos(c))
"""

def third_side(a, b, angle_C_deg):
    # Convert angle from degrees to radians
    angle_C_rad = math.radians(angle_C_deg) # 3.14

    # Apply law of Cosines
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_C_rad))
    return c


print(third_side(5, 8, 49))  
# 6.04339
