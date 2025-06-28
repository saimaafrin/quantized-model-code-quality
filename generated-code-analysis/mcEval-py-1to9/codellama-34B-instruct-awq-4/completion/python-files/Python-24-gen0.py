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
    # Base case, when n is smaller than k*x
    if n < k * x:
        return 0

    # Initialize a 2d array to store the results of subproblems
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]

    # Initialize the first row
    for i in range(n + 1):
        dp[0][i] = 1

    # Fill in the dp table
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i * x > j:
                dp[i][j] = 0
            else:
                dp[i][j] = sum(dp[i - 1][j - p] for p in range(i * x, j + 1))

    return dp[k][n]
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