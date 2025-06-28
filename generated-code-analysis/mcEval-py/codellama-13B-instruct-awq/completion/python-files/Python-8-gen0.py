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
    # Check if the number of grid values exceeds the size of the grid.
    if len(grid_values) > N:
        raise ValueError('The number of grid values exceeds the size of the grid.')

    # Create the grid and fill it with zeroes.
    grid: List[List[int]] = [[0 for i in range(N)] for j in range(N)]

    # Fill the grid with the grid values.
    for row, col, value in grid_values:
        if 0 <= row < N and 0 <= col < N:
            grid[row][col] = value

    # Create the maximum value arrays.
    max_value_left: List[List[int]] = [[0 for i in range(N)] for j in range(N)]
    max_value_right: List[List[int]] = [[0 for i in range(N)] for j in range(N)]

    # Fill the maximum value arrays with the grid values.
    for row in range(N):
        for col in range(N):
            if row == 0 and col == 0:
                max_value_left[row][col] = grid[row][col]
                max_value_right[row][col] = grid[row][col]
            elif row == 0 and col > 0:
                max_value_left[row][col] = grid[row][col] + max_value_left[row][col - 1]
                max_value_right[row][col] = grid[row][col] + max_value_right[row][col - 1]
            elif col == 0 and row > 0:
                max_value_left[row][col] = grid[row][col] + max_value_left[row - 1][col]
                max_value_right[row][col] = grid[row][col] + max_value_right[row - 1][col]
            else:
                max_value_left[row][col] = max(grid[row][col] + max_value_left[row - 1][col],
                                               grid[row][col] + max_value_left[row][col - 1])
                max_value_right[row][col] = max(grid[row][col] + max_value_right[row - 1][col],
                                                grid[row][col] + max_value_right[row][col - 1])

    # Find the maximum sum of values collected on both paths.
    max_sum: int = 0
    for row in range(N):
        for col in range(N):
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