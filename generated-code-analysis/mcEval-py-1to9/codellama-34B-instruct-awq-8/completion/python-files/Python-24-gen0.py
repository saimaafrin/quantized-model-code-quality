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
    # Special case 1: If the number of parts is 1, the only way to
    # partition the number is to assign the entire number to the part.
    if k == 1:
        return 1

    # Special case 2: If the minimum value for each part is greater
    # than the number to be partitioned, the only way to partition
    # the number is to assign the entire number to the part.
    if x > n:
        return 1

    # Initialize a 2D array to store the number of distinct partitioning
    # ways for each partition size.
    dp = [[0] * (x + 1) for _ in range(k + 1)]

    # Initialize the top row and leftmost column with 1's.
    for i in range(k + 1):
        dp[i][0] = 1
    for j in range(x + 1):
        dp[0][j] = 1

    # Fill in the remaining cells in the 2D array by iterating over each
    # partition size j and number i.
    for j in range(1, x + 1):
        for i in range(1, n + 1):
            # The number of ways to partition i into j parts is equal to
            # the sum of the number of ways to partition i-j into j parts
            # and the number of ways to partition i-j into j-1 parts.
            dp[j][i] = dp[j][i - j] + dp[j - 1][i - j]

    # The number of ways to partition n into k parts, where each part is
    # at least x, is equal to the sum of the number of ways to partition
    # n-kx into k parts, where each part is at least x, and the number of
    # ways to partition n-kx into k-1 parts, where each part is at least x.
    return dp[k][n - k * x]
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