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

    # check length
    if k == 1:
        return [grid[0][0]]
    
    # find row and col
    row = len(grid)
    col = len(grid[0])

    # init path
    path = [[-1 for j in range(col)] for i in range(row)]
    path[0][0] = 0

    # traverse
    for i in range(row):
        for j in range(col):
            # check out of bound
            if i + 1 < row and path[i + 1][j] != -1 and path[i][j] == -1:
                path[i][j] = path[i + 1][j] + 1
            if j + 1 < col and path[i][j + 1] != -1 and path[i][j] == -1:
                path[i][j] = path[i][j + 1] + 1
            if i + 1 < row and j + 1 < col and path[i + 1][j + 1] != -1 and path[i][j] == -1:
                path[i][j] = path[i + 1][j + 1] + 1
    
    # find start
    start = (0, 0)
    while start[0] < row and start[1] < col:
        if path[start[0]][start[1]] != -1:
            break
        start = (start[0] + 1, start[1] + 1)

    # trace
    lst = []
    row, col = start
    while len(lst) < k:
        lst.append(grid[row][col])
        next_row, next_col = -1, -1
        if row + 1 < row and path[row + 1][col] != -1:
            next_row = row + 1
            next_col = col
        elif col + 1 < col and path[row][col + 1] != -1:
            next_row = row
            next_col = col + 1
        elif row + 1 < row and col + 1 < col and path[row + 1][col + 1] != -1:
            next_row = row + 1
            next_col = col + 1
        row = next_row
        col = next_col
