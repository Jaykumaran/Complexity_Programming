# https://www.geeksforgeeks.org/check-whether-point-exists-circle-sector-not/

"""
Convert x, y to polar coordinates using this 
    Angle = atan(y/x); Radius = sqrt(x * x + y * y);
Then Angle must be between StartingAngle and EndingAngle, and Radius between 0 and your Radius.
"""
import math

def point_exists_sector(radius, x, y, sectorpercent, startAngle):

    # Calc end angle
    endAngle = 360 / percent + startAngle

    # Calc polar coords
    polar_radius = math.sqrt(x * x + y * y)
    Angle = math.atan(y/x)   # m = tan(theta)  

    # Check whether angle is between startAngle and endAngle
    # Check whether polar_radius is less than radius of circle or not
    if (Angle >= startAngle and Angle <= endAngle) and polar_radius < radius:
        print("Yes, the point exist within circle sector")
    else:
        print("Doesn't exist in the circle sector")
      
radius, x, y = 8, 3, 4
percent, startAngle = 12, 0
 
point_exists_sector(radius, x, y, percent, startAngle)

    
