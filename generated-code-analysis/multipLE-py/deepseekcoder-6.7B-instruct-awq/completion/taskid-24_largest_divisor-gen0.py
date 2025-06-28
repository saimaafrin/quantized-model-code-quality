def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """


    # Initialize the divisor as the largest possible number (which is n - 1)
    divisor = n - 1

    # While the divisor is greater than 0
    while divisor > 0:
        # If n is divisible by the divisor, return the divisor
        if n % divisor == 0:
            return divisor
        # Otherwise, decrement the divisor
        else:
            divisor -= 1
