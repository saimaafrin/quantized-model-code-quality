from typing import List, Tuple

def max_value_on_paths(N: int, grid_values: List[Tuple[int, int, int]]) -> int:
    """
    Calculate the maximum sum of values collected on two paths in an N x N grid.

    This function utilizes dynamic programming to find two paths from the top-left corner to
    the bottom-right corner of the grid which maximize the sum of the values collected. Each
    value can be collected at most once, even if both paths pass through it.

    Args:
    - N (int): The size of the grid (N x N).
    - grid_values (List[Tuple[int, int, int]]): A list of tuples where each tuple contains
      the x-coordinate, y-coordinate, and value to be placed on the grid at that position.
      The list is terminated by a tuple with all zeros.

    Returns:
    - int: The maximum sum of values collected on the two paths.

    Examples:
    >>> max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)])
    3
    >>> max_value_on_paths(8, [
    ...     (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
    ...     (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
    ...     (0, 0, 0)])
    67
    """

    grid = [[0] * N for _ in range(N)]

    # Populate the grid with the given values.
    for i in range(N):
        for j in range(N):
            x, y, value = grid_values[i * N + j]
            grid[x][y] = value

    # dp[i][j] is the maximum value that can be collected by a path starting at (0, 0) and
    # ending at (i, j), where 0 <= i < N and 0 <= j < N.
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = grid[0][0]

    # Iterate over each cell in the grid, calculating the maximum value that can be
    # collected from each cell and storing it in dp.
    for i in range(1, N):
        for j in range(N):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # dp_sum is the maximum value that can be collected from the grid by traversing any two
    # paths.
    dp_sum = 0
    for i in range(N):
        for j in range(N):
            dp_sum = max(dp_sum, dp[i][j] + grid[i][j] - dp[i - 1][j - 1])

    return dp_sum
def test_max_value_on_paths():
    # Test case 1: Small grid with clear path
    assert max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)]) == 3
    
    # Test case 2: Example provided in the problem statement
    assert max_value_on_paths(8, [
        (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
        (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
        (0, 0, 0)]) == 67

    print("All test cases passed!")

# Run the test cases
test_max_value_on_paths()