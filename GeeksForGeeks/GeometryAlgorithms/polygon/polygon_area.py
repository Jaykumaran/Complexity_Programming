# https://www.geeksforgeeks.org/area-of-a-polygon-with-given-n-ordered-vertices/

def polygon_area(X, Y):
    n = len(X)
    area = 0
    for i in range(n):
        # j should be i+1 because y_i+1 
        j = (i + 1) % n # next vertex index, wraps around to 0
        """
      Shoelace Formula:
        Area = 1/2 * |(x0*y1 + x1*y2 + ... + xn-1*y0) - (y0*x1 + y1*x2 + ... + yn-1*x0)|

      Parameters:
        X (list of float or int): List of x-coordinates of the polygon vertices.
        Y (list of float or int): List of y-coordinates of the polygon vertices.
        """
        area += (X[i] * Y[j]) - (Y[i] * X[j])

    return abs(area) / 2

X1 = [0, 4, 4, 0]
Y1 = [0, 0, 4, 4],
print("Area:", polygon_area(X1, Y1))  # Output: 16.0


X2 = [0, 4, 2]
Y2 = [0, 0, 4]
print("Area:", polygon_area(X2, Y2))  # Output: 8.0
