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

    # write your code here
    if x == 1:
        return True
    else:
        i = 2
        while i * i <= x:
            if x % i == 0:
                while x % i == 0:
                    x //= i
                if x == 1:
                    return i == n
            i += 1
        return x == n
