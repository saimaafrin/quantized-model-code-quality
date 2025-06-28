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

    # Initialize dp table
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base case: n is zero
    for i in range(n+1):
        dp[i][0] = 1

    # Base case: k is zero
    for j in range(n+1):
        dp[0][j] = 0

    # Base case: k is one
    for i in range(n+1):
        dp[i][1] = 1 if i >= x else 0

    # Base case: n is less than x
    for j in range(n+1):
        dp[j][j] = 0 if j < x else 1

    # Calculate dp values
    for i in range(1, n+1):
        for j in range(2, min(i, k)+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-j][j]

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