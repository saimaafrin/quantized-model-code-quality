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

    # Initialize a grid of size N x N with zeros
    grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # Fill in the grid with the given values
    for x, y, value in grid_values:
        grid[x][y] = value

    # Initialize a dp array of size 2*N+1 x 2*N+1 with negative infinity
    dp = [[-float('inf') for _ in range(2*N + 1)] for _ in range(2*N + 1)]

    # The base case is when the current position is the bottom-right corner of the grid
    dp[N][N] = grid[N][N]

    # Calculate the maximum sum of values collected on the two paths
    for s in range(2*N - 1, -1, -1):
        for x1 in range(max(0, s - N), min(N, s) + 1):
            y1 = s - x1
            for x2 in range(x1, N + 1):
                y2 = s - x2
                best = max(dp[x1+1][y1], dp[x1][y1+1], dp[x1+1][y1+1], dp[x1][y1])
                if (x1, y1) == (x2, y2):  # The paths do not overlap
                    dp[x1+1][y1+1] = best + grid[x1+1][y1+1]
                else:  # The paths overlap
                    dp[x1+1][y1+1] = dp[x2+1][y2+1] = best + grid[x1+1][y1+1] + grid[x2+1][y2+1]

    # Return the maximum sum of values collected on the two paths
    return dp[1][1]
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