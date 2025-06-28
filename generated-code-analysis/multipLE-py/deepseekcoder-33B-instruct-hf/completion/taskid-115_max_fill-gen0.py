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

    if capacity == 0:
        return 0
    grid = grid[::-1]  # Invert the grid, so we start from the lowest well
    levels = [0 for _ in range(len(grid[0]))]  # Array to keep track of the water levels
    bucket_count = 0  # Count of times we need to lower the bucket
    for well in grid:
        for i, water in enumerate(well):
            levels[i] += water  # Add the water in the current well to the water level
            if levels[i] > capacity:  # If the water level is greater than the bucket capacity
                bucket_count += 1  # We need to lower the bucket
                levels[i] = water  # And start filling it again
    return bucket_count
