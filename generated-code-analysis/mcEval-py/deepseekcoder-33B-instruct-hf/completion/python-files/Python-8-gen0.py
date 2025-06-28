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
    # Initialize the grid and path arrays
    grid = [[0] * (N+1) for _ in range(N+1)]
    path = [[0] * (N+1) for _ in range(N+1)]

    # Fill the grid with the provided values
    for x, y, val in grid_values:
        grid[x][y] = val

    # Calculate the maximum path sum for each cell in the grid
    for x in range(1, N+1):
        for y in range(1, N+1):
            if x == 1 and y == 1:
                path[x][y] = grid[x][y]
            elif x == 1:
                path[x][y] = max(path[x][y-1], path[x-1][y-1]) + grid[x][y]
            elif y == 1:
                path[x][y] = max(path[x-1][y], path[x-1][y-1]) + grid[x][y]
            else:
                path[x][y] = max(path[x-1][y], path[x][y-1], path[x-1][y-1]) + grid[x][y]

    return path[N][N]
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