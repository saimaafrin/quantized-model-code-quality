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
    grid = [[0] * (N + 1) for _ in range(N + 1)]
    dp1 = [[0] * (N + 1) for _ in range(N + 1)]
    dp2 = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(len(grid_values) - 1):
        x, y, val = grid_values[i]
        grid[x][y] = val

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1]) + grid[i][j]

    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1]) + grid[i][j]

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ans = max(ans, dp1[i][j] + dp2[i][j] - grid[i][j])

    return ans
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