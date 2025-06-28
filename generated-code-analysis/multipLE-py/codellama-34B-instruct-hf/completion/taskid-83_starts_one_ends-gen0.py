def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def starts_ends(n: int) -> int:
        """
        Args:
            n: Number of digits of the number.

        Returns:
            The number of numbers of n-digit positive integers that start
            or end with 1.
        """

        if n == 1:
            return 2

        return 2 * (10**(n - 1) - 1)

    return starts_ends(n) + starts_ends(n - 1)
