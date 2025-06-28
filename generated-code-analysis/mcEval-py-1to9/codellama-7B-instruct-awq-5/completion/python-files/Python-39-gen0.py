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
    def number_of_ways_to_arrange_pots(n, m, a) -> int:
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
        - number_of_ways_to_arrange_pots(2, 4, [3, 2]) returns 12.
        - number_of_ways_to_arrange_pots(3, 3, [1, 2, 3]) returns 3.
        """
        # Initialize the maximum number of pots for each flower type.
        max_pots = [0] * n
        for i in range(n):
            max_pots[i] = a[i]

        # Initialize the number of ways to arrange the pots.
        ways = [0] * (m + 1)
        ways[0] = 1

        for i in range(1, m + 1):
            # Get the number of pots to arrange.
            num_pots = min(max_pots[i - 1], m - i + 1)

            # Initialize the number of ways to arrange the current pots.
            ways[i] = 0

            # Check each combination of flower types.
            for j in range(num_pots, 0, -1):
                # Check each flower type.
                for k in range(n, 0, -1):
                    # Check if the current flower type can be used.
                    if max_pots[k - 1] < j:
                        continue

                    # Check if the current arrangement is valid.
                    if i < j:
                        continue

                    # Increment the number of ways to arrange the pots.
                    ways[i] = (ways[i] + ways[i - j]) % 1000000

                    # Reduce the number of pots available for the current flower type.
                    max_pots[k - 1] -= j
                    break

        return ways[m]

    return number_of_ways_to_arrange_pots(n, m, a)
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