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

    # Initialize the grid
    grid = [[0]*N for _ in range(N)]
    for x, y, val in grid_values:
        if x == 0 and y == 0:
            break
        grid[y-1][x-1] = val

    # Initialize the dp table
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = grid[0][0]

    # Initialize the path
    path = [[0]*N for _ in range(N)]
    path[0][0] = grid[0][0]

    # Fill in the dp table
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1, N):
        for j in range(1, N):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                path[i][j] = path[i-1][j] + grid[i][j]
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                path[i][j] = path[i][j-1] + grid[i][j]

    # Find the maximum sum of values on the two paths
    max_val = max(max(row) for row in dp)

    return max_val
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