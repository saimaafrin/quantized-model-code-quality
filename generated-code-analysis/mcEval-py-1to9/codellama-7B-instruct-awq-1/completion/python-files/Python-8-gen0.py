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

    # Initialize a 2-dimensional grid.
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # Populate the grid with the values.
    for row, col, value in grid_values:
        grid[row][col] = value

    # Initialize dynamic programming variables.
    dp_up = [[0 for _ in range(N)] for _ in range(N)]
    dp_down = [[0 for _ in range(N)] for _ in range(N)]

    # Initialize the top-left and bottom-right squares.
    dp_up[0][0] = grid[0][0]
    dp_down[N-1][N-1] = grid[N-1][N-1]

    # Initialize the top and bottom rows.
    dp_up[0][1:N] = dp_up[1:N][0]
    dp_down[N-1][0:N-1] = dp_down[N-2][N-1]

    # Initialize the left column.
    dp_up[1:N][0] = dp_up[1:N][1]
    dp_down[0:N-1][N-1] = dp_down[0:N-2][N-1]

    # Calculate the maximum sum of values collected on two paths.
    max_value = 0
    for row in range(N):
        for col in range(N):
            max_value = max(max_value, dp_up[row][col] + dp_down[row][col])

    return max_value
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