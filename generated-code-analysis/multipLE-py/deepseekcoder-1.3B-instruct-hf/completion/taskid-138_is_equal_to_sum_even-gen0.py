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

    def is_even(num: int) -> bool:
        return num % 2 == 0

    def is_sum_of_four_even(n: int) -> bool:
        for i in range(1, n + 1):
            if n - i >= 0 and is_even(n - i) and is_even(i):
                if (n - i - i) > 0 and is_even(n - i - i):
                    return True
        return False

    return is_sum_of_four_even(n)
