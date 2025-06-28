def choose_num(x: int, y: int) -> int:
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    >>> choose_num(12, 15)
    14
    >>> choose_num(13, 12)
    -1
    """

    x = x % 2
    y = y % 2
    if x == 0 and y == 0:
        return -1
    elif x == 0:
        return max(y, 0)
    else:
        return max(x, 0)
