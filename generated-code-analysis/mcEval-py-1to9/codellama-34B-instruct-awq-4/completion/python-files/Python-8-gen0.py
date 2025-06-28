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
    # Initialize a grid of (0, 0) coordinates to mark which values have been collected.
    grid = [[(0, 0) for _ in range(N)] for _ in range(N)]

    # Fill in the values in the grid, keeping track of the maximum value found.
    max_value = 0
    for x, y, value in grid_values:
        grid[x][y] = (x, y)
        max_value = max(max_value, value)

    # Initialize a table with all values set to the minimum value.
    table = [[0] * (N + 1) for _ in range(N + 1)]
    for row in table:
        row[0] = -max_value

    # Fill in the table using the recurrence relation.
    for row_idx in range(1, N + 1):
        for col_idx in range(1, N + 1):
            if grid[row_idx - 1][col_idx - 1] == (row_idx - 1, col_idx - 1):
                table[row_idx][col_idx] = max(
                    table[row_idx - 1][col_idx],
                    table[row_idx][col_idx - 1],
                    table[row_idx - 1][col_idx - 1] + max_value)
            else:
                table[row_idx][col_idx] = max(
                    table[row_idx - 1][col_idx],
                    table[row_idx][col_idx - 1],
                    table[row_idx - 1][col_idx - 1])

    # The maximum value is the last value in the last row of the table.
    return table[N][N]
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