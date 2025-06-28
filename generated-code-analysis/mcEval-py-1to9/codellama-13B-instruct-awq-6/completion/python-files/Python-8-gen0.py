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
    # Initialize a two-dimensional array for the maximum values that can be collected on each
    # path to the bottom-right corner of the grid.
    #
    # The first index of the array corresponds to the starting position on the path, and the
    # second index corresponds to the x-coordinate.
    #
    # The values in the array represent the maximum sum of values that can be collected on the
    # path to the bottom-right corner of the grid, assuming that only the values from the
    # starting position to the current position are collected.
    dp: List[List[int]] = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the maximum value to be collected on the first path.
    dp[0][0] = grid_values[0][2]

    # Iterate through the x-coordinates of the grid.
    for x in range(1, N + 1):
        # Initialize the maximum value to be collected on the second path.
        dp[1][x] = grid_values[x - 1][2]

        # Iterate through the y-coordinates of the grid.
        for y in range(2, N + 1):
            # Determine the maximum value to be collected on the two paths at the current
            # position.
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

            # Check if the current position contains a value.
            if grid_values[x - 1][0] == y - 1 and grid_values[x - 1][1] == x - 1:
                # Update the maximum value to be collected on the first path.
                dp[y][x] = max(dp[y][x], dp[y - 1][x] + grid_values[x - 1][2])

    # Return the maximum sum of values collected on the two paths.
    return dp[N][N]
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