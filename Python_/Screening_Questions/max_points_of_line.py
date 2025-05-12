# Max Points on a Line (LeetCode #149)

"""Solution 1: n3 with three for loops, and can be fixed with a hasmap
Go through all the pair of points 
"""

"""
Solution2: Find slope wrt to the first point and save it in a hashmap
# Consider sample: points = [[1, 1], [2, 2], [3, 3]]

# Assume:
  - Atleast one point is given

# slope = (y2 - y1) / (x2 - x1)
"""

from typing import List

def max_points(points: List[List[int]]) -> int:
    res = 1 # atleast one point exists to start
    for i in range(len(points)): # i = 0, 1, 2
        p1 = points[i]           # p1 = [1, 1] on first iteration
        count = {}  # hashmap to store slopes from p1
        # Dont consider the first point now, for finding the pair of points slope
        for j in range(i+ 1, len(points)):  # j = 1, 2
            p2 = points[j]            # [2, 2]
            # Check whether both points are in vertical , 
            #i.e. same x value, (y2 - y1)/ 0 as it may throw zero div error
            # so set it to inf
  
            if p2[0] == p1[0]:        # Here: 2 != 1
               slope = float('inf')
            else:
               slope = (p2[1] - p1[1]) /  (p2[0] - p1[0]) # (2 -1) / (2 - 1) = 1.0

            # Check count logic # 1.0 is already in count
            if slope not in count: # for eg: a slope of 2 is already there, check any other slope value is there btw the
               count[slope] = 1
            else:
               # count[1.0] = 2
               count[slope] += 1   # increase the count of that particular slope if same m is found with other point

            res = max(res, count[slope] + 1)
    return res
               
            
result = max_points([[1, 1], [2, 2], [3, 3]])
print(result) # 3


"""
1.Initialize a variable to store the maximum number of points on the same line, initially set to 1.
2.Iterate through each point (P1) in the given list of points.
3. For each point (P1), initialize a hash map to store the count of points with the same slope.
4. For each subsequent point (P2) in the list of points, excluding P1, calculate the slope between P1 and P2.
5. Store the slope in the hash map, incrementing the count for that slope.
6. Keep track of the maximum count of points with the same slope.
7.Handle coincident points separately by counting them and updating the maximum count accordingly.
8. Repeat steps 3–7 for all points in the list.
10. After iterating through all the points, the maximum count of points with the same slope is the answer to the problem.

"""
         
        
    
