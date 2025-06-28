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

    # Put your code here
    if a < b and a < c:
        a, c = c, a
    elif b < a and b < c:
        b, c = c, b

    return c**2 == a**2 + b**2
