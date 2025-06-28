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

    # Create a table to store results of subproblems
    dp = [[[0 for _ in range(n + 1)] for _ in range(k + 1)] for _ in range(x + 1)]

    # Fill dp[][][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(1, x + 1):
                # If l is more than i, then i cannot be the first part
                if l > i:
                    dp[i][j][l] = dp[i][j][l - 1]

                # If l is same as i and j is more than 1, then i cannot be the first part
                elif l == i and j > 1:
                    dp[i][j][l] = dp[i][j - 1][l]

                # If l is less than or equal to i and j is 1, then count the partition ways
                elif l <= i and j == 1:
                    dp[i][j][l] = dp[i - l][j][l] + 1

                # If l is less than or equal to i and j is more than 1, then count the partition ways
                else:
                    dp[i][j][l] = dp[i - l][j - 1][l] + dp[i][j][l - 1]

    # Return the number of ways to partition n into k parts with minimum part l
    return dp[n][k][x]
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