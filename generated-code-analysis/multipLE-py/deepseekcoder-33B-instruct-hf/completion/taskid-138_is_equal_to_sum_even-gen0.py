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

    return n in [
        2 + 4 + 6 + 8,
        2 + 4 + 6 + 12,
        2 + 4 + 8 + 10,
        2 + 6 + 8 + 10,
        4 + 6 + 8 + 10,
        2 + 4 + 6 + 10,
        2 + 4 + 8 + 12,
        2 + 6 + 8 + 12,
        4 + 6 + 8 + 12,
        2 + 4 + 10 + 12,
        2 + 6 + 10 + 12,
        4 + 6 + 10 + 12,
        2 + 8 + 10 + 12,
        4 + 8 + 10 + 12,
        6 + 8 + 10 + 12,
        2 + 4 + 6 + 14,
        2 + 4 + 8 + 14,
        2 + 6 + 8 + 14,
        4 + 6 + 8 + 14,
        2 + 4 + 10 + 14,
        2 + 6 + 10 + 14,
        4 + 6 + 10 + 14,
        2 + 8 + 10 + 14,
        4 + 8 + 10 + 14,
        6 + 8 + 10 + 14,
    ]
