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

    # Initialize a 2D grid with zeros
    grid = [[0]*N for _ in range(N)]

    # Populate the grid with values
    for x, y, value in grid_values:
        grid[x-1][y-1] = value

    # Define the direction vectors
    dir_x = [1, 0]
    dir_y = [0, 1]

    # Initialize a 3D dp table with zeros
    dp = [[[0]*2 for _ in range(N)] for _ in range(N)]

    # Initialize the dp table
    for s in range(N):
        for d in range(2):
            dp[N-1][s][d] = sum(grid[i][s] for i in range(s, N))

    # Populate the dp table
    for r in range(N-2, -1, -1):
        for s in range(N):
            for d in range(2):
                dp[r][s][d] = grid[r][s] + max(
                    dp[r+dir_x[d]][s+dir_y[d]][d],
                    max(dp[r][s+1][0], dp[r][s+1][1]) if s+1 < N else 0
                )

    # Return the maximum sum of values collected
    return max(dp[0][0][0], dp[0][0][1])
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