# Find minimum radius such that atleast k point lie inside the circle

# https://www.geeksforgeeks.org/find-minimum-radius-atleast-k-point-lie-inside-circle/


def min_radius_squared(points, k):
    # Calculate squares of distances from origin
    """
    The Euclidean distance between two points (x1, y1) and (x2, y2) is:

        distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    Distance from point (x, y) to the origin (0, 0), this becomes:

        distance = sqrt(x^2 + y^2)

    We use x^2 + y^2 to avoid square root since we only compare distances.
    """
    distances = [x**2 + y**2 for x, y in points]  # Compute squared distances
    distances.sort()  # Sort distances
    return distances[k - 1]  # Return the k-th smallest (0-indexed)

points = [(1, 1), (-1, -1), (1, -1)]
k = 3
print(min_radius_squared(points, k))  # 2
