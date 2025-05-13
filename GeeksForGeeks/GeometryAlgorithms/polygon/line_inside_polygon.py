# https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/

def is_point_in_polygon(x, y, polygon):
    n = len(polygon)  # total number of vertices
    inside = False    # To track if point is inside the polygon
    k = 0 # intersection count

    px1, py1 = polygon[0]  # start with first vertex
    for i in range(n + 1):  # +1 for the first point to be included as closure
        # Loop through each edge (wrap around at the end)
        px2, py2 = polygon[i % n]  # Get the next vertex (modulo wraps to first at the end)

        # Check if point y is between the y values of the current edge  
        # min(y1, y2) < y <= max(y1, y2)
        if y > min(py1, py2):
            if y <= max(py1, py2):
                # check if point x is to the left of the edge 
                if x <= max(px1, px2):
                    # Avoid zero division: need to make sure the edge is not horizontal
                    if py1 != py2:
                        # Calculate x-coordinate of the intersection point with the edge
                        # x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                        x_intersect = (y - py1) * (px2 - px1) / (py2 - py1) + px1

                    # If the point is to the left of the intersection (or on it), flag 'inside'
                    if px1 == px2 or x <= x_intersect:
                        inside = not inside  # Toggle inside status, True
                        k += 1 # odd or even

        # Move to next edge
        px1, py1 = px2, py2

    return inside, k


polygon = [(0, 0), (10, 0), (10, 10), (0, 10)]
point = (5, 5)

print(is_point_in_polygon(point[0], point[1], polygon))  
# True, 1


      
        
    
