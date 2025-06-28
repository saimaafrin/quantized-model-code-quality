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


    n_rows = len(grid)
    n_cols = len(grid[0])

    def _get_max_fill(i: int, j: int) -> int:
        # i, j is the top-left corner of the square
        # and the bottom-right corner is (i + width, j + width)
        width = min(n_rows - i, n_cols - j)
        max_fill = 0

        for k in range(0, width):
            for l in range(0, width):
                max_fill = max(max_fill, grid[i + k][j + l])
        return max_fill

    dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    dp[0][0] = _get_max_fill(0, 0)

    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0 and j == 0:
                continue

            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

            if dp[i][j] > capacity:
                return -1
    return dp[n_rows - 1][n_cols - 1]
