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
    # Build a grid that keeps track of the maximum values along each path from the top-left
    # corner to each position in the grid.
    max_values = [[0] * N for _ in range(N)]

    # The maximum values for the top-left corner are the values in the first row.
    for y, (x, _, value) in enumerate(grid_values):
        if x == 0 and y == 0:
            max_values[y][x] = value

    # Initialize the first column and row with the values in the first row and column.
    for y in range(1, N):
        max_values[y][0] = max(max_values[y - 1][0], grid_values[y][2])

    for x in range(1, N):
        max_values[0][x] = max(max_values[0][x - 1], grid_values[x][2])

    # Fill in the rest of the grid with the maximum values.
    for y in range(1, N):
        for x in range(1, N):
            max_values[y][x] = max(
                max_values[y - 1][x],
                max_values[y][x - 1],
                grid_values[y][2])

    return max_values[N - 1][N - 1]
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