import math


def brute_force_minimum(pts):
    min_dist = float('inf')
    best_pair = None
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            d = dist(pts[i], pts[j])
            if d < min_dist:
               min_dist = d
               best_pair(pts[i], pts[j])
    return min_dist, best_pair


def closest_pair(points):
   def distance(a,b): # Euclidean distance
       return math.hypot(a[0]-b[0], a[1]-b[1])

   # recursively solve
   def solve(pts):
       # For 2 or 3 points, just check all pairs and return the minimum distance and the pair.
       if len(pts) <= 3: # Use brute force when <= 3
          return brute_force_minimum(pts)
         
        # Otherwise
        # Divide the points into two halves and solve recursively
        mid = len(pts) // 2
        # smallest distance in each half
        # p1 p2 : closest pairs in each half
        d1, p1 = solve(pts[:mid]) 
        d2, p2 = solve(pts[mid:]) 
        d, best_pair = min((d1, p1), (d2, p2))

        mx = pts[mid][0]
        """Is there a pair of points, one from the left half and one from the right half, that are closer than d? If such a pair exists, 
        it must be the true closest pair overall for this set of pts. This is what the "strip" logic aims to find."""
        strip = [p for p in pts if abs(p[0] - mx) < d]
        strip.sort(key = lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if strip[j][1] - strip[i][1] >= d:
                    break
                new_d = distance(strip[i], strip[j])
                if new_d < d:
                   d, best_pair = new_d, (strip[i], strip[j])
        return d, best_pair

    points.sort()
    return solve(points)

        
