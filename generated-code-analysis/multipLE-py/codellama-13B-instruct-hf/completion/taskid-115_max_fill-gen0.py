from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    # number of rows
    n = len(grid)
    # number of columns
    m = len(grid[0])

    # number of buckets
    num_buckets = 1

    # iterate over the buckets
    while num_buckets <= capacity:

        # iterate over each row
        for i in range(n):

            # initialize a temporary sum variable
            sum = 0

            # iterate over each column
            for j in range(m):

                # if the current cell is 1, add the bucket to the sum
                if grid[i][j] == 1:
                    sum += 1

                # if the sum equals the number of buckets, return the number of buckets
                if sum == num_buckets:
                    return num_buckets

        # iterate over the buckets
        num_buckets += 1

    # if the function reaches the end without returning a value, return None
    return None
