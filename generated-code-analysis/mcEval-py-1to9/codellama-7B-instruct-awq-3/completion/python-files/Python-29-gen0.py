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
    # Solution: Iterative approach using binary search.
    # Since the harmonic series grows logarithmically, we can use a binary search approach to find the smallest n
    # that satisfies the condition. We can start with an initial estimate for n and repeatedly adjust the estimate
    # until we find the smallest n that works.
    # Time complexity: O(log n)
    # Space complexity: O(1)

    # Initialize the lower and upper bounds for the binary search.
    lower_bound = 1
    upper_bound = 2**32 - 1

    # Iteratively perform the binary search until we find the smallest n that works.
    while True:
        # Calculate the midpoint of the current interval.
        midpoint = (lower_bound + upper_bound) // 2

        # Calculate the harmonic series sum for the current midpoint.
        harmonic_sum = sum(1.0 / i for i in range(1, midpoint + 1))

        # Check if the harmonic series sum exceeds the threshold k.
        if harmonic_sum > k:
            # If the harmonic series sum exceeds the threshold k, adjust the upper bound for the binary search.
            upper_bound = midpoint
        else:
            # If the harmonic series sum does not exceed the threshold k, adjust the lower bound for the binary search.
            lower_bound = midpoint + 1

        # Check if the current interval is 1 long.
        if upper_bound - lower_bound == 1:
            # If the interval is 1 long, return the smallest integer in the interval.
            return lower_bound
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