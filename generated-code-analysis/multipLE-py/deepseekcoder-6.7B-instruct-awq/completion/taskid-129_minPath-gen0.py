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

    N = len(grid)
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    dp = [[[float("inf")]*k for _ in range(N)] for _ in range(N)]
    parent = [[[(None, None)]*k for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dp[i][j][0] = grid[i][j]

    for l in range(1, k):
        for x in range(N):
            for y in range(N):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if dp[nx][ny][l-1] > dp[x][y][l-1] + grid[nx][ny]:
                            dp[nx][ny][l] = dp[x][y][l-1] + grid[nx][ny]
                            parent[nx][ny][l] = (x, y)

    min_val = float("inf")
    min_pos = None
    for x in range(N):
        for y in range(N):
            if dp[x][y][k-1] < min_val:
                min_val = dp[x][y][k-1]
                min_pos = (x, y)

    path = []
    x, y = min_pos
    for l in range(k-1, -1, -1):
        path.append(grid[x][y])
        x, y = parent[x][y][l]

    return path[::-1]
