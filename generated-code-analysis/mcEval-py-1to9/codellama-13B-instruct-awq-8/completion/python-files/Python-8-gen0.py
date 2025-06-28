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
    # Initialize the grid to contain zeros.
    grid = [[0] * N for _ in range(N)]

    # Populate the grid with values.
    for x, y, value in grid_values:
        grid[x - 1][y - 1] = value

    # Initialize the memoization table for the maximum sums.
    sums = [[0] * N for _ in range(N)]
    sums[0][0] = grid[0][0]

    # Initialize the memoization table for the paths.
    paths = [[(0, 0)] * N for _ in range(N)]
    paths[0][0] = (0, 0)

    # Fill in the memoization table for the maximum sums.
    for x in range(1, N):
        for y in range(N):
            if grid[x][y] == 0:
                continue

            sums[x][y] = max(
                sums[x - 1][y] + grid[x][y],
                sums[x][y - 1] + grid[x][y]
            )
            paths[x][y] = (x - 1, y) if sums[x][y] == sums[x - 1][y] + grid[x][y] else (x, y - 1)

    # Find the maximum sum by returning the maximum of the sums of the
    # two paths from the top-left corner to the bottom-right corner.
    return max(
        sums[N - 1][y] for y in range(N)
    )
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