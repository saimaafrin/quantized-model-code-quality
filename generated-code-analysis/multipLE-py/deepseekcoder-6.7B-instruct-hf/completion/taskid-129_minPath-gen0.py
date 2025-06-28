from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:    
    >>> minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
    [1, 2, 1]

    >>> minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1)
    [1]
    """

    n = len(grid)
    dp = [[[float('inf')] * n * n for _ in range(n)] for _ in range(k+1)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0] * n for _ in range(n)] for _ in range(k+1)]
    for x in range(n):
        for y in range(n):
            dp[1][x][y] = grid[x][y]
            visited[1][x][y] = True
    for l in range(2, k+1):
        for x in range(n):
            for y in range(n):
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and visited[l-1][nx][ny]:
                        dp[l][x][y] = min(dp[l][x][y], dp[l-1][nx][ny] + grid[x][y])
                visited[l][x][y] = dp[l][x][y] != float('inf')
    min_val = min(dp[k][x][y] for x in range(n) for y in range(n))
    res = []
    for l in range(k, 0, -1):
        for x in range(n):
            for y in range(n):
                if dp[l][x][y] == min_val and visited[l][x][y]:
                    res.append(grid[x][y])
                    min_val = min((dp[l-1][nx][ny] for nx, ny in [(x+dx[i], y+dy[i]) if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n else (0, 0) for i in range(4)] + [float('inf')]))
                    break
            else:
                continue
            break
    return res[::-1]
