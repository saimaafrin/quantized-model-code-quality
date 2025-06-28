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
    # Initialize the dynamic programming table.
    # Each cell contains a tuple of the maximum value that can be collected on a path from
    # the top-left corner of the grid to that cell and the x-coordinate of the previous cell
    # on that path.
    dp = [[(0, 0) for _ in range(N)] for _ in range(N)]

    # Populate the dynamic programming table with the values given in the grid.
    for x, y, v in grid_values:
        dp[y][x] = (v, x)

    # Iterate over each cell in the grid and update the dynamic programming table.
    for y in range(N):
        for x in range(N):
            # Update the dynamic programming table for the cell at coordinates (x, y).
            if dp[y][x][0] != 0:
                # The cell at coordinates (x, y) contains a value, so we need to calculate
                # the maximum sum of values collected on a path that passes through it.
                up_x, up_y = x, y - 1
                left_x, left_y = x - 1, y
                # Check if the cell above the current cell contains a value.
                if 0 <= up_y < N and dp[up_y][up_x][0] != 0:
                    # The cell above the current cell contains a value, so we add it to the
                    # maximum sum of values collected on a path that passes through the
                    # current cell.
                    dp[y][x] = max(dp[y][x], (dp[up_y][up_x][0] + dp[y][x][0], up_x))
                # Check if the cell to the left of the current cell contains a value.
                if 0 <= left_x < N and dp[left_y][left_x][0] != 0:
                    # The cell to the left of the current cell contains a value, so we add
                    # it to the maximum sum of values collected on a path that passes
                    # through the current cell.
                    dp[y][x] = max(dp[y][x], (dp[left_y][left_x][0] + dp[y][x][0], left_x))

    # Iterate over each cell in the grid and find the maximum sum of values collected on
    # a path that passes through it.
    max_value = 0
    x, y = 0, 0
    while dp[y][x][0] != 0:
        # Calculate the maximum sum of values collected on a
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