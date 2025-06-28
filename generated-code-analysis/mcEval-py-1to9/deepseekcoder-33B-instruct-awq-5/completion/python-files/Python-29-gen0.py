def find_min_n_greater_than_k(k: int) -> int:
    """
    Calculate the smallest positive integer n such that the sum of the harmonic series
    up to 1/n is greater than a given positive integer k.

    The harmonic series is defined as S_n = 1 + 1/2 + 1/3 + ... + 1/n.

    Args:
    - k (int): A positive integer representing the threshold value the harmonic series sum must exceed.

    Returns:
    - int: The smallest integer n for which the harmonic series sum S_n exceeds the threshold k.

    Examples:
    >>> find_min_n_greater_than_k(1)
    2
    >>> find_min_n_greater_than_k(3)
    11
    """
    from fractions import Fraction

    # Initialize the harmonic sum.
    harmonic_sum = Fraction(0, 1)

    # Start with n = 1.
    n = 1

    # Keep adding the next fraction to the harmonic sum until it exceeds k.
    while harmonic_sum < k:
        n += 1
        harmonic_sum += Fraction(1, n)

    # Return the smallest n for which the harmonic sum exceeds k.
    return n
def test_find_min_n_greater_than_k():
    # Test case 1: k = 1, expected result is 2

    assert find_min_n_greater_than_k(1) == 2, "Test case 1 failed."

    # Test case 2: k = 3, expected result is 11
    assert find_min_n_greater_than_k(3) == 11, "Test case 2 failed."
    # Test case 3: k = 5, expected result is 83
    assert find_min_n_greater_than_k(5) == 83, "Test case 3 failed."

    print("All test cases passed.")


# Run the test function
test_find_min_n_greater_than_k()