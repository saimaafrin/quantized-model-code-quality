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
    # Initialize the number of arrangements to 0.
    arrangements = 0
    # Iterate through all the possible arrangements.
    for combination in itertools.product(range(n), repeat=m):
        # Initialize the current arrangement to be the empty list.
        current = []
        # Iterate through all the elements in the combination.
        for element in combination:
            # Append the element to the current arrangement.
            current.append(element)
            # Check if the length of the current arrangement is greater than the maximum number of pots.
            if len(current) > a[element]:
                # Break out of the inner loop.
                break
        # Check if the length of the current arrangement is equal to the length of the combination.
        if len(current) == len(combination):
            # Increment the number of arrangements.
            arrangements += 1
    # Return the number of arrangements modulo (10^6 + 7).
    return arrangements % (10**6 + 7)
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