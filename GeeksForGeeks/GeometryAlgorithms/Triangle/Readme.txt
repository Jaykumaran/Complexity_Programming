dy = y2- y1
dx = x2 - x1

Handle and Check whether they are horizontal or vertical line

Pick's theorem:
    I = A - B/2 + 1
------------------------------------------------------------------


Valid Triangle Given three sides
- The sum of two sides must be greater than the third side

------------------------------------------------------------------

Cosine law:
    opposite of the angle side = a^2 + b^2 - 2ab cos(angle)

------------------------------------------------------------------
Dot product
        AB = (x2 - x1, y2 - y1)


 """
    Compare dot product and cross product usage.

    | Purpose                | Dot Product                         | Cross Product                |
    |------------------------|-----------------------------------|--------------------------------|
    | Result                 | Scalar (number)                   | Vector                         |
    | Angle Relation         | Uses cos(θ)                       | Uses sin(θ)                    |
    | Perpendicularity Check | Dot product = 0                   | Cross product = zero vector    |
    | Find Perpendicular Vec | No                                | Yes                            |
    | Calculate Area         | No                                | Yes                            |

    Explanation:

    Dot Product:
      - Formula: u · v = u_x*v_x + u_y*v_y + u_z*v_z
      - Measures how much two vectors point in the same direction.
      - Useful to find angle between vectors, projection, and orthogonality.

    Cross Product:
      - Formula: u × v = (u_y*v_z - u_z*v_y, u_z*v_x - u_x*v_z, u_x*v_y - u_y*v_x)
      - Produces a vector perpendicular to both u and v.
      - Useful to find perpendicular vector, area of parallelogram, and orientation.
    """

