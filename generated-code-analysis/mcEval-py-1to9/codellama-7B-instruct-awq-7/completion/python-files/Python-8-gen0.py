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
    # Dynamic programming grid. Each element contains the maximum sum of values collected
    # along the two paths in the grid up to that point.
    dp_grid = [[0] * N for _ in range(N)]
    for x, y, value in grid_values:
        dp_grid[x][y] = value
    for x in range(N):
        for y in range(N):
            # For each position in the grid, look at the maximum value that can be collected
            # from the two paths that end there.
            left_value = max(
                dp_grid[x - 1][y] + dp_grid[x][y - 1],
                dp_grid[x - 1][y - 1] + dp_grid[x][y],
            )
            right_value = max(
                dp_grid[x][y - 1] + dp_grid[x - 1][y],
                dp_grid[x - 1][y] + dp_grid[x][y],
            )
            dp_grid[x][y] = max(left_value, right_value)
    return dp_grid[N - 1][N - 1]
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