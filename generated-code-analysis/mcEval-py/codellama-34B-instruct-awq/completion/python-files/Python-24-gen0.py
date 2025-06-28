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

    # The solution uses dynamic programming.
    # For details, see https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Partition_function_formulas
    # It uses the recurrence relation: p(n,k) = p(n-k,k) + p(n-1,k-1) + p(n-2,k-1) + ...
    # The solution assumes k >= x. If k < x, the result is 0.

    # The main diagonal corresponds to the partition (n,1)
    # The matrix is initialized with the values p(n,1).
    # This corresponds to the first row of the partition table.
    dp = [1] + [0] * (k - 1)

    for i in range(n):
        # The first element of the row (the diagonal) corresponds to the partition (i+1,1)
        dp.insert(0, 0)
        for j in range(1, k + 1):
            # The recurrence relation
            dp[j] = dp[j - 1] + dp[j]

    return dp[k]
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