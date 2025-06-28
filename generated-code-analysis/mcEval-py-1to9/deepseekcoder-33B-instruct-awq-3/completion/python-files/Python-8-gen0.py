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
    MAX_N = 100
    MAX_VAL = 1000
    INF = 10**9
    dp = [[[-INF]*MAX_N for _ in range(MAX_N)] for _ in range(MAX_N)]
    grid = [[0]*MAX_N for _ in range(MAX_N)]
    for x, y, val in grid_values:
        grid[x][y] = val
    dp[0][0][0] = grid[0][0]
    for n in range(1, N+N-1):
        for x1 in range(max(0, n-N), min(N, n+1)):
            y1 = n-x1
            for x2 in range(max(0, n-N), x1+1):
                y2 = n-x2
                v = max(
                    dp[x1-1][y1][x2-1] if x1>0 and y2>0 else -INF,
                    dp[x1-1][y1][x2] if x1>0 else -INF,
                    dp[x1][y1-1][x2-1] if y1>0 and x2>0 else -INF,
                    dp[x1][y1-1][x2] if y1>0 else -INF)
                v += grid[x1][y1]
                if x1 != x2 or y1 != y2:
                    v += grid[x2][y2]
                dp[x1][y1][x2] = v
    return max(dp[N-1][N-1][N-1], 0)
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