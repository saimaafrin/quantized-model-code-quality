def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    if n == 1:
        return 1
    else:
        return 10 + 9 * 9 ** (n - 2)
