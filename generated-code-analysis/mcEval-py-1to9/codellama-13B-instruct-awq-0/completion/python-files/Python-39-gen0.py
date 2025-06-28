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
    def mod_add(a, b):
        return (a + b) % (10 ** 6 + 7)

    # Compute the number of arrangements recursively, using dynamic programming.
    # Since the arrangements are in increasing order of flower types, we only need to consider the first
    # flower type to determine the number of arrangements for the first m flowers.
    # We compute the number of arrangements for m flowers using the recurrence relation:
    # number_of_arrangements[m] = sum(number_of_arrangements[m - j] * number_of_arrangements[j - 1]
    #                                  for j in range(1, min(m + 1, n + 1)))
    # where the sum is taken over the possible number of flowers of the first flower type.
    # The base case is when m = 0, where there is only one arrangement (i.e., an empty arrangement).
    number_of_arrangements = [0] * (m + 1)
    number_of_arrangements[0] = 1
    for i in range(1, m + 1):
        # If there are no flowers left to place, there is only one arrangement.
        if i == 0:
            number_of_arrangements[i] = 1
            continue

        # Otherwise, compute the number of arrangements using the recurrence relation.
        number_of_arrangements[i] = 0
        for j in range(1, min(i + 1, n + 1)):
            number_of_arrangements[i] = mod_add(number_of_arrangements[i],
                                                 number_of_arrangements[i - j] * number_of_arrangements[j - 1])

    return number_of_arrangements[m]
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