def x_or_y(n: int, x: int, y: int) -> int:
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """


    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    if is_prime(n):
        return x
    else:
        return y
