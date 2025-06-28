def is_simple_power(x: int, n: int) -> bool:
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    >>> is_simple_power(1, 4)
    True
    >>> is_simple_power(2, 2)
    True
    >>> is_simple_power(8, 2)
    True
    >>> is_simple_power(3, 2)
    False
    >>> is_simple_power(3, 1)
    False
    >>> is_simple_power(5, 3)
    False
    """

    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        for i in range(1, x):
            if n**i == x:
                return True
        return False
