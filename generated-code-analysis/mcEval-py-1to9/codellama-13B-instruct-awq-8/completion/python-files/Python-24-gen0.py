def count_partitions(n: int, k: int, x: int) -> int:
    """
    Count the number of ways to partition an integer n into k parts,
    where each part is at least x and order of parts does not matter.

    Parameters:
    n (int): The integer to be partitioned.
    k (int): The number of parts to divide n into.
    x (int): The minimum value for each part.

    Returns:
    int: The number of distinct partitioning ways.

    Examples:
    >>> count_partitions(7, 3, 1)
    4
    >>> count_partitions(6, 2, 1)
    3
    """
    # Set up the 2D array for the dp table.
    # dp[i][j] represents the number of ways to partition i into j parts.
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Fill the dp table using the recurrence relation.
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Base case: if j == 1, then the only way to partition i is i.
            if j == 1:
                dp[i][j] = 1
            # Recurrence relation: if j > 1, then partition i into j parts.
            else:
                # Case 1: The last part is at least x.
                dp[i][j] += dp[i - x][j - 1]
                # Case 2: The last part is less than x.
                dp[i][j] += dp[i - 1][j]

    return dp[n][k]
def test_count_partitions():
    # Test case 1: Simple case
    result = count_partitions(7, 3, 1)
    assert result == 4, f"Expected 4, got {result}"

    # Test case 2: Another simple case
    result = count_partitions(6, 2, 1)
    assert result == 3, f"Expected 3, got {result}"

    # Test case 3: Partitioning into a larger number of parts
    result = count_partitions(8, 4, 1)
    assert result == 5, f"Expected 5, got {result}"

    print("All test cases passed successfully!")


# Call the test function to run the test cases
test_count_partitions()