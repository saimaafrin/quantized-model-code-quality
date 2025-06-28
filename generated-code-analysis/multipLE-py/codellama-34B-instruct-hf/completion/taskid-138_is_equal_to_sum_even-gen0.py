def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """

    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                for d in range(c, n):
                    if a + b + c + d == n:
                        if (a + b + c + d) % 2 == 0:
                            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
                                return True
    return False
