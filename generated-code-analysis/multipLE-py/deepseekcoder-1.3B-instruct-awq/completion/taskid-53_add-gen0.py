def add(x: int, y: int) -> int:
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

    if x >= y:
        return x + y
    else:
        return y + x
