def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Since each digit can be 0-9, except for the first and last digit,
    # we can subtract the count of 9-digit numbers from the total count
    # of n-digit numbers.
    total = 9 * (10 ** (n - 1))
    if n == 1:
        return 1
    else:
        return total - starts_one_ends(n - 1)
