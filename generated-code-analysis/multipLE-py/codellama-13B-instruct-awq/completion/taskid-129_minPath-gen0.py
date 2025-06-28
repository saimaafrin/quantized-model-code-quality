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

    m = len(grid)
    n = len(grid[0])

    if m != n:
        raise ValueError("Grid must be square")

    # initialize dist array to store shortest path length
    dist = [[float('inf') for i in range(n)] for j in range(n)]

    # initialise distance of 0 between a node and itself
    for i in range(n):
        dist[i][i] = 0

    # initialise distance of 1 between each adjacent nodes
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = 1

    # initialise a priority queue to store nodes to be processed
    pq = []

    # initialise a dictionary to store minimum distance from source node
    minDist = {}

    # initialise the source node to have shortest distance of 0
    minDist[(0, 0)] = 0

    # initialise a dictionary to store parent of each node
    parent = {}

    # initialise the parent of source node to itself
    parent[(0, 0)] = (0, 0)

    # push the source node into the priority queue
    heappush(pq, (0, 0))

    # while the priority queue is not empty
    while len(pq):
        # extract the minimum distance node from the priority queue
        node = heappop(pq)

        # check if we have reached the destination node
        if node[0] == n - 1 and node[1] == n - 1:
            # break from the loop if we have reached the destination node
            break

        # iterate through each of the adjacent nodes of the extracted node
        for i in range(n):
            # calculate the distance of the adjacent nodes of the extracted node
            newDist = dist[node[0]][node[1]] + dist[node[1]][i]

            # check if the distance of the adjacent node is less than the current minimum distance
            if newDist < minDist[(i, node[1])]:
                # update the minimum distance of the adjacent node
                minDist[(i, node[1])] = newDist

                # update the parent of the adjacent node
                parent[(i, node[1])] = (node[0], node[1])

                # push the adjacent node into the priority queue
                he
