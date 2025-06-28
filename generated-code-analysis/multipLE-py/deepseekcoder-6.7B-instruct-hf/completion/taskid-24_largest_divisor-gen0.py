def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Start by checking for the biggest possible divisor
    # in this case, that would be half of the number, because no number can be
    # bigger than half of it that can divide a number evenly
    i = n // 2
    while i > 0:
        if n % i == 0:
            return i
        i -= 1
