def right_angle_triangle(a: int, b: int, c: int) -> bool:
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    >>> right_angle_triangle(3, 4, 5)
    True
    >>> right_angle_triangle(1, 2, 3)
    False
    """

    # find the square of the shortest side
    shortest_side_sq = min(a * a, b * b, c * c)
    # find the square of the longest side
    longest_side_sq = max(a * a, b * b, c * c)
    # check if the shortest side squared is equal to the sum of the other two sides squared
    return shortest_side_sq == (longest_side_sq - (a * a + b * b))
