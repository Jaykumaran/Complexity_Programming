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

         
        
    
