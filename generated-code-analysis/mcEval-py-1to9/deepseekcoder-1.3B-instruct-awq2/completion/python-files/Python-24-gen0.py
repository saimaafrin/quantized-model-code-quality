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
    # This is a straightforward dynamic programming problem.
    # Create a 3D array to store the number of ways to partition n into k parts.
    # Initialize the first row and first column with 1 (since the number of ways to partition 0 into 0 parts is 1).
    dp = [[[0 for _ in range(x)] for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(k + 1):
            for l in range(x):
                if i == 0 or j == 0:
                    dp[i][j][l] = 0
                elif i < l * j:
                    dp[i][j][l] = dp[i][j][l - 1]
                else:
                    dp[i][j][l] = dp[i][j - 1][l] + dp[i - l][j - 1][l]
    return dp[n][k][x - 1]
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