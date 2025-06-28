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

    # A list of size (n-x*k) to store the number of ways to get each part
    count = [0] * (n - x * k)
    count[0] = 1

    # Iterate through all possible remaining parts
    for i in range(k):
        # Iterate through all possible sums of parts
        for j in range(n - x * k, 0, -1):
            # If j - x can be divided by j,
            # it means that the sum of all remaining parts is divisible by j
            # and we add the number of ways to get the previous parts
            if (j - x) % j == 0:
                count[j - x] += count[j]

    return count[0]
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