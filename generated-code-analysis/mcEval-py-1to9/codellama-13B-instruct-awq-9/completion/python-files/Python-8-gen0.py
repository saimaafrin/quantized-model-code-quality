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
    # Initialize the grid with a single path of zeroes
    grid = [[[0, 0]] for _ in range(N)]

    # Populate the grid with the values given by the user
    for i, j, value in grid_values:
        grid[i - 1][j - 1] = [[value, value], [0, 0]]

    # Update the grid by iterating over the rows
    for i in range(N):
        # Update the grid by iterating over the columns
        for j in range(N):
            # Initialize a variable to store the maximum value from the left
            left_max = 0

            # If the left neighbor is not a wall, then take its maximum value
            if grid[i][j - 1][0] != -1:
                left_max = grid[i][j - 1][0]

            # Initialize a variable to store the maximum value from the above
            above_max = 0

            # If the above neighbor is not a wall, then take its maximum value
            if grid[i - 1][j][0] != -1:
                above_max = grid[i - 1][j][0]

            # If the current position is not a wall, then take its value
            if grid[i][j][0] != -1:
                current = grid[i][j][0]
            else:
                current = 0

            # Calculate the maximum value from the current position
            max_value = max(left_max, above_max, current)

            # Set the maximum value for the current position
            grid[i][j][0] = max_value

            # Calculate the sum of values from the current position to the end
            sum_values = max_value + grid[i][j][1]

            # Set the sum of values for the current position
            grid[i][j][1] = sum_values

    # Return the maximum sum of values collected on the two paths
    return grid[N - 1][N - 1][1]
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