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
    def recurse(n_types, m_pots, a):
        if n_types == 0:
            return 1
        elif m_pots == 0:
            return 0
        else:
            result = 0
            for i in range(max(1, m_pots - a[n_types - 1]), m_pots + 1):
                result += recurse(n_types - 1, i, a)
            return result % (10**6 + 7)
    return recurse(n, m, a)
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