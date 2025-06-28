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

    # Initialize the grid.
    grid = [[0] * N for _ in range(N)]

    # Initialize the maximum sum of values collected on both paths.
    max_sum = 0

    # Fill in the grid values.
    for (x, y, value) in grid_values:
        grid[x-1][y-1] = value

    # Initialize the dynamic programming tables.
    path_values_1 = [[0] * N for _ in range(N)]
    path_values_2 = [[0] * N for _ in range(N)]

    # Initialize the values at the bottom-right corner of the grid.
    path_values_1[-1][-1] = grid[-1][-1]
    path_values_2[-1][-1] = grid[-1][-1]

    # Fill in the dynamic programming tables.
    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            path_values_1[i][j] = max(path_values_1[i+1][j], path_values_1[i][j+1]) + grid[i][j]
            path_values_2[i][j] = max(path_values_2[i+1][j], path_values_2[i][j+1]) + grid[i][j]

    # Calculate the maximum sum of values collected on both paths.
    for i in range(N):
        max_sum = max(max_sum, path_values_1[0][i] + path_values_2[0][i])

    return max_sum
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