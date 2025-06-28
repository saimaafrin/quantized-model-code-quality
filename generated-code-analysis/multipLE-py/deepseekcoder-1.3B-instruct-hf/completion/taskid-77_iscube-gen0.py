def iscube(a: int) -> bool:
    """
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    """


    # check if input is negative, if so return False
    if a < 0:
        return False

    # compute cube root and check if integer
    cube_root = a ** (1/3)
    return cube_root.is_integer()
