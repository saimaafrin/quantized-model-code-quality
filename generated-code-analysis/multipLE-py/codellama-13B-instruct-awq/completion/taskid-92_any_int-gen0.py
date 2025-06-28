def any_int(x: float, y: float, z: float) -> bool:
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    >>> any_int(5, 2, 7)
    True
    
    >>> any_int(3, 2, 2)
    False

    >>> any_int(3, -2, 1)
    True
    
    >>> any_int(3.6, -2.2, 2)
    False
  

    
    """

    # Solution 1
    # return isinstance(x, int) and isinstance(y, int) and isinstance(z, int) and (x+y==z or x+z==y or y+z==x)

    # Solution 2
    return ((x == int(x) and y == int(y) and z == int(z))
            and (x + y == z or x + z == y or y + z == x))

    # Solution 3
    # return (x == int(x) and y == int(y) and z == int(z)) and any(
    #     (x+y) == z, (x+z) == y, (y+z) == x
    # )
