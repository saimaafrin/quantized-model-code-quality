def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # The largest number smaller than n and divisible by n are the largest divisor of n
    # since we start from the largest number and go down to 1
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
