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

    if n < 6 or n % 2 != 0:
        return False
    s = 0
    e = 0
    for i in range(2, n, 2):
        s += i
        e += 1
    return s == n and e == 4
