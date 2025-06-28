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

    # Base case 1: No more water to fill
    if not any(row for row in grid):
        return 0
    # Base case 2: No more capacity to fill
    if capacity == 0:
        return -1
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    buckets_required = 0
    # Iterate through each row
    for row in range(rows):
        # Find the first 1 from the right
        first_one = next((i for i, val in enumerate(grid[row][::-1]) if val), -1)
        # If no 1s found, this row is filled
        if first_one == -1:
            continue
        # Calculate how many buckets are required for this row
        buckets_required += first_one
        # If we exceed capacity, return -1
        if buckets_required > capacity:
            return -1
        # Fill the bucket, and empty the well
        capacity -= first_one
        for col in range(cols):
            grid[row][col] = 0
    # Recursively check each well
    for row in range(rows):
        # Fill the well, and decrement the number of buckets
        capacity -= grid[row][0]
        grid[row][0] = 0
        # If we exceed capacity, return -1
        if capacity < 0:
            return -1
    # If we have no more capacity to fill, return buckets used
    if capacity == 0:
        return buckets_required
    # Otherwise, recursively check the next row
    return max_fill(grid, capacity)
