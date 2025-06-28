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
    # Create a grid of all zeros.
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # Place the grid values on the grid.
    for x, y, value in grid_values:
        grid[x][y] = value

    # Initialize the dynamic programming grid.
    dp_grid = [[0 for _ in range(N)] for _ in range(N)]

    # Start by finding the maximum value on one path.
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                continue

            if j == N - 1:
                dp_grid[i][j] = grid[i][j]
            else:
                dp_grid[i][j] = max(
                    dp_grid[i][j],
                    dp_grid[i][j + 1] + grid[i][j])

    # Start by finding the maximum value on the other path.
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if grid[i][j] == 0:
                continue

            if j == 0:
                dp_grid[i][j] = grid[i][j]
            else:
                dp_grid[i][j] = max(
                    dp_grid[i][j],
                    dp_grid[i][j - 1] + grid[i][j])

    # Return the maximum sum of values collected.
    return max(dp_grid[0][0], dp_grid[0][N - 1], dp_grid[N - 1][0], dp_grid[N - 1][N - 1])
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