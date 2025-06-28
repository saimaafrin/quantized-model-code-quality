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
    # check if we can't divide n into k parts with each part >= x
    if n < k * x or n > (k + 1) * x:
        return 0
    # base case: if k == 0 and n == 0, we've found a valid partitioning
    if k == 0 and n == 0:
        return 1
    # if we have no more partitions to make, but n > 0, no valid partitioning
    if k == 0:
        return 0
    # if n < k * x, no valid partitioning
    if n < k * x:
        return 0
    # if n == 0 but k > 0, no valid partitioning
    if n == 0:
        return 0
    # count the number of ways to partition n - x into k - 1 parts
    # and the number of ways to partition n into k - 1 parts
    return count_partitions(n - x, k - 1, x) + count_partitions(n, k - 1, x)
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