# https://www.geeksforgeeks.org/section-formula-point-divides-line-given-ratio/

# Formula: [mx2 + nx1 / m+n, my2 + ny1 / m + n]

def section(x1, y1, x2, y2, m, n):
    x = ((m * x2) + (n * x1))/ (m + n)
    y = ((m * y2) + (n * y1)) / (m + n)
    return (x, y)


         
