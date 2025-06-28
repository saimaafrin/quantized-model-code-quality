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

    # Initialize the maximum sum of values collected for each cell in the grid to zero.
    # The cell at the top-left corner will hold the maximum sum of values collected for
    # the two paths from the top-left corner to the bottom-right corner.
    grid = [[0 for _ in range(N)] for _ in range(N)]

    # Each value can be collected at most once, even if both paths pass through it.
    collected_values = set()

    for x, y, value in grid_values:
        if (x, y) in collected_values:
            continue

        collected_values.add((x, y))
        grid[x][y] = value

    for x in range(N):
        for y in range(N):
            if (x, y) in collected_values:
                continue

            left_value = grid[x][y]
            right_value = grid[x][y]

            if x > 0:
                left_value = grid[x-1][y] + grid[x][y]

            if y > 0:
                right_value = grid[x][y-1] + grid[x][y]

            grid[x][y] = max(left_value, right_value)

    return grid[N-1][N-1]
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