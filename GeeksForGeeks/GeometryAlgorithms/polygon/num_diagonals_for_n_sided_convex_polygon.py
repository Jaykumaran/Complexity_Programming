# https://www.geeksforgeeks.org/find-number-diagonals-n-sided-convex-polygon/

"""
Since for an n-sided convex polygon, from each vertex, we can draw n-3 diagonals leaving
two adjacent vertices and itself. Following this way for n-vertices, there will be n*(n-3) diagonals but 
then we will be calculating each diagonal twice so total number of diagonals become n*(n-3)/2
"""

def numberOfDiagonals(n):
    return n * (n-3) / 2


def main():
    n = 5
    res = numberOfDiagonals(n)
    print(res)

if __name__ == '__main__':
   main()
