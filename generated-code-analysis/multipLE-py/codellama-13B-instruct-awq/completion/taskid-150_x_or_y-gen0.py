def x_or_y(n: int, x: int, y: int) -> int:
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """

    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return y
    else:
        return y
    return x
