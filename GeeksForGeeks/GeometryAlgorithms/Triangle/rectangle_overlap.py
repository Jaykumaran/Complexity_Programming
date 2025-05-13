# https://www.geeksforgeeks.org/find-two-rectangles-overlap/

def rectanglesOverlap(l1,r1,l2,r2):

    """
    Check:
      1) r1 left of l2; r2 left of l1
      2) l1 below r2 or l2 below r1

    """
    # Just approach using False conditions
    if r1[0] <= l2[0] or r2[0] <= l1[0]:
        return False

    if l1[1] <= r2[1] or l2[1] <= r1[1]:
        return False

    return True


l1 = (0, 10)
r1 = (10, 0)
l2 = (5, 5)
r2 = (15, 0)

if rectanglesOverlap(l1, r1, l2, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Don’t Overlap")
      
      
