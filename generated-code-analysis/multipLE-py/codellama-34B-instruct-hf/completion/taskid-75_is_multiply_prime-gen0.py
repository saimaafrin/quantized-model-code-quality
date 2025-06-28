def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    for x in range(2, a):
        for y in range(2, a):
            for z in range(2, a):
                if x * y * z == a:
                    return True
    return False
