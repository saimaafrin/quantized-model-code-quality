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
    grid = [[0] * N for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    for x, y, value in grid_values:
        grid[x - 1][y - 1] = value
    dp[0][0] = grid[0][0]
    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    max_value = dp[-1][-1]
    paths = [[(N - 1, N - 1)]]
    i, j = N - 1, N - 1
    while i != 0 or j != 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            j -= 1
        else:
            paths.append(paths[-1][:-1] + [(i - 1, j), (j, i - 1)])
            i -= 1
            j -= 1
        paths[-1].append((i, j))
    for path in paths:
        for x, y in path:
            grid[x][y] = 0
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for i in range(1, N):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, N):
            for j in range(1, N):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        max_value = max(max_value, dp[-1][-1])
        for x,
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