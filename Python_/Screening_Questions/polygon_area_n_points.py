""" Find the polygon area of n points given coordinates of those points
# Shoelace formula:
    Area = ½ × |Σ (xᵢ·yᵢ₊₁ − xᵢ₊₁·yᵢ)|   for i = 0 to n-1 """


# list of coords is passed
def polygon_area(coords):
    n = len(coords) # number of vertices
    area = 0

    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+ 1) % n]  # wrap to form a closed loop for the last point back to 0
        area += (x1 * y2) - (x2 * y1)

    return abs(area)/2

coords = [(0, 0), (4, 0), (4, 3), (0, 3)]  # rectangle
n = 4
polygon_area(coords)
# 12.0
        
    
    

