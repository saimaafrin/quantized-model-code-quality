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

    # Test if the number is even
    if n % 2 != 0:
        return False

    # Set a list of possible numbers to add together to make n
    nums = [i for i in range(2, n)]

    # Test if the numbers summed together is greater than n
    if sum(nums) > n:
        return False

    # Test if the numbers summed together is less than n
    elif sum(nums) < n:
        return False

    # Return True if the numbers summed together is equal to n
    return True
