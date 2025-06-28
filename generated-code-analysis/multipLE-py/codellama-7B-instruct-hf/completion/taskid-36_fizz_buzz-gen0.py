def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    if n <= 0:
        raise ValueError("n should be a positive integer.")

    counter = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i) == "7" * i:
                counter += 1

    return counter
