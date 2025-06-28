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
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # Fill in the values of the grid.
    for grid_value in grid_values:
        grid[grid_value[0]][grid_value[1]] = grid_value[2]

    # Initialize the dynamic programming table.
    table = [[[0, 0] for _ in range(N)] for _ in range(N)]

    # Initialize the table with the values at the top left.
    table[0][0] = grid[0][0]

    # Fill in the table using the recurrence.
    for i in range(1, N):
        table[0][i] = max(table[0][i-1], grid[0][i] + table[0][i-1][1])

    for j in range(1, N):
        table[j][0] = max(table[j-1][0], grid[j][0] + table[j-1][0][1])

    for i in range(1, N):
        for j in range(1, N):
            table[i][j] = [
                max(table[i][j-1], grid[i][j] + table[i][j-1][1]),
                max(table[i-1][j], grid[i][j] + table[i-1][j][0])]

    # Return the maximum sum.
    return max(table[N-1][N-1])
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