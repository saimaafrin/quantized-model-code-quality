def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 10
    if n == 2:
        return 90

    count = 0
    for i in range(10, 10**n):
        num_str = str(i)
        if num_str[0] == '1' or num_str[-1] == '1':
            count += 1
    return count
