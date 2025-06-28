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
    # Setup the grid to store the maximum sum of values collected on the two paths from
    # each cell to the bottom-right corner of the grid.
    grid = [[0] * N for _ in range(N)]
    # Set the final cell of the grid to the maximum value collected on a path.
    grid[-1][-1] = grid_values[-1][2]

    # Fill in the grid with the maximum sum of values collected on the two paths from
    # each cell to the bottom-right corner of the grid.
    for y in range(N - 2, -1, -1):
        for x in range(N - 2, -1, -1):
            # Collect the value at the current cell.
            value = grid_values[x + y * N][2]
            # Find the maximum sum of values collected on the two paths from the current
            # cell to the bottom-right corner of the grid.
            grid[x][y] = max(grid[x + 1][y], grid[x][y + 1]) + value

    # Return the maximum sum of values collected on the two paths from the top-left corner
    # to the bottom-right corner of the grid.
    return grid[0][0]
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