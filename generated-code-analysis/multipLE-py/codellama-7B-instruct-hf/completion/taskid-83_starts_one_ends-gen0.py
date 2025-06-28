def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start = 10 ** (n - 1) + 1
    end = 10 ** n
    return sum(int(i) for i in range(start, end) if str(i)[0] == '1'
               or str(i)[-1] == '1')
