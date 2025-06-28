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


    # Solution
    rows, cols = len(grid), len(grid[0])
    max_well_water = 0
    max_bucket_capacity = capacity
    water_level = rows - 1
    bucket_level = 0
    num_moves = 0
    while water_level > 0:
        num_moves += 1
        max_well_water = max(max_well_water, grid[water_level][bucket_level])
        if max_well_water > max_bucket_capacity:
            num_moves += 1
            max_well_water -= max_bucket_capacity
        if max_well_water == 0:
            water_level -= 1
            if water_level > 0:
                max_well_water = grid[water_level][bucket_level]
        else:
            max_well_water = 0
        if bucket_level < cols - 1 and grid[water_level][bucket_level + 1] > 0:
            bucket_level += 1
        else:
            water_level -= 1
            bucket_level = 0
    return num_moves
