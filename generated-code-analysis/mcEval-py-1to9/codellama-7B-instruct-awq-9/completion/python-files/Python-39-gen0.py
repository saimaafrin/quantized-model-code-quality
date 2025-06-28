def calculate_arrangements(n, m, a) -> int:
    """
    Compute the number of ways to arrange m pots of flowers using up to n types,
    where the ith type can have at most a[i] pots, and the arrangement must be in
    increasing order of flower types.

    Args:
    - n (int): The number of flower types available.
    - m (int): The total number of flower pots to arrange.
    - a (list of int): A list where a[i] is the maximum number of pots for the ith type of flower.

    Returns:
    - int: The number of distinct arrangements modulo (10^6 + 7).

    Examples:
    - calculate_arrangements(2, 4, [3, 2]) returns 2.
    - calculate_arrangements(3, 3, [1, 2, 3]) returns 6.
    """
    # Base cases.
    if m < n or m < 0:
        return 0
    if m == 0:
        return 1

    # Recursive cases.
    total_arrangements = 0
    for i in range(1, n+1):
        # For each type of flower, compute the number of arrangements that include it.
        # The number of arrangements that include the current type of flower is the
        # number of arrangements that include the previous types minus the number
        # of arrangements that include the previous types that are greater than the
        # current type.
        # For example, if we have 3 flower types, and we have 4 pots total, and we are
        # currently looking at the first flower type, there are 4 - 3 = 1 arrangement
        # that includes the first flower type.
        # If we are currently looking at the second flower type, there are 4 - 2 = 2
        # arrangements that include the second flower type.
        # If we are currently looking at the third flower type, there are 4 - 1 = 3
        # arrangements that include the third flower type.
        num_arrangements_including_current_type = m - (m - i)
        total_arrangements += num_arrangements_including_current_type * calculate_arrangements(n-1, m-i, a)

    return (total_arrangements + 10**6) % (10**6 + 7)
def test_calculate_arrangements():
    # Helper function to compare expected and actual results
    def assert_equal(actual, expected, message):
        assert actual == expected, message

    # Test Case 1
    n, m, a = 2, 4, [3, 2]
    expected = 2
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 1 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 2
    n, m, a = 3, 3, [1, 2, 3]
    expected = 6
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 2 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 3
    n, m, a = 1, 5, [5]
    expected = 1
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 3 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    print("All tests passed!")

if __name__ == "__main__":
    test_calculate_arrangements()