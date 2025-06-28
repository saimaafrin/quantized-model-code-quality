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
    def count_partitions_recursive(n: int, k: int, x: int, p: list = None) -> int:
        """
        Recursive function to count the number of partitions.

        Parameters:
        n (int): The integer to be partitioned.
        k (int): The number of parts to divide n into.
        x (int): The minimum value for each part.
        p (list): The partition, which should be empty when the function is called for the first time.

        Returns:
        int: The number of distinct partitioning ways.
        """
        # Initialize the partition if it is not provided
        if not p:
            p = [0] * k

        # Base case 1: If n is 0, return 1
        if n == 0:
            return 1

        # Base case 2: If n is less than x, return 0
        if n < x:
            return 0

        # Base case 3: If the number of parts is 1, return 1
        if k == 1:
            return 1

        # Initialize the count of partitions to 0
        count = 0

        # Loop over all possible values that the current part can take
        for i in range(min(n, x), 0, -1):
            p[k - 1] = i

            # Call the function recursively for the next part
            count += count_partitions_recursive(n - i, k - 1, x, p)

        return count

    # Call the recursive function to get the number of partitions
    return count_partitions_recursive(n, k, x)
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