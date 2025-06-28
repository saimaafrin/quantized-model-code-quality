def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """

    total = 1
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 != 0:
            total *= last_digit
        n = n // 10
    return total
