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
    # Initialize an accumulator variable to store the running sum
    s = 0.0

    # Iterate from 1 to infinity
    for i in range(1, float('inf')):
        # Calculate the harmonic series sum up to the current value of i
        s += 1.0 / i

        # If the sum exceeds the threshold value k, return the current value of i as the solution
        if s > k:
            return i

    # If the threshold value k is not reached, return None
    return None
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