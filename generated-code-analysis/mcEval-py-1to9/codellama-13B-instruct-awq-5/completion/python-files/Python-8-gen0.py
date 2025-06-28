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
    # Initialize the grid to have a value of -1 (unassigned) at each position.
    grid = [[-1 for _ in range(N)] for _ in range(N)]

    # Assign values to grid positions based on the input grid_values.
    for v in grid_values:
        x, y, value = v
        grid[x][y] = value

    # Initialize the two paths to have a value of -1 (unassigned) at each position.
    path1 = [[-1 for _ in range(N)] for _ in range(N)]
    path2 = [[-1 for _ in range(N)] for _ in range(N)]

    # Initialize the sum of the values collected on each path to 0.
    sum_path1 = 0
    sum_path2 = 0

    # The maximum sum of values collected on the two paths.
    max_sum = 0

    # Initialize the current position to the top-left corner.
    x = 0
    y = 0

    # Initialize the path to have a value of -1 (unassigned).
    path_value = -1

    # While the current position is not the bottom-right corner.
    while x < N - 1 or y < N - 1:
        # If the current position is unassigned or has a larger value than the
        # current maximum sum of values collected on the two paths.
        if grid[x][y] == -1 or grid[x][y] > max_sum:
            # Update the maximum sum of values collected on the two paths.
            max_sum = max(max_sum, grid[x][y])

            # If the path value is unassigned or has a larger value than the
            # current maximum sum of values collected on the two paths.
            if path_value == -1 or path_value > max_sum:
                # Update the path value.
                path_value = max_sum

            # If the path value is the maximum sum of values collected on the two paths.
            if path_value == max_sum:
                # Update the sum of values collected on the current path.
                sum_path1 += grid[x][y]

                # If the current position is the bottom-right corner.
                if x == N - 1 and y == N - 1:
                    # Update the sum of values collected on the other path.
                    sum_path2 += grid[x][y]

                    # Return the sum of values collected on the two paths.
                    return sum_path1 + sum_path2

        # Update the position.
        if x == N -
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