def optimize_seating(M: int, N: int, K: int, L: int, D: int, chatting_pairs: list) -> (str, str):
    """
    Optimize the placement of aisles in a classroom to minimize the amount of chatting between students.

    Args:
    M (int): The number of rows in the classroom.
    N (int): The number of columns in the classroom.
    K (int): The number of horizontal aisles to add.
    L (int): The number of vertical aisles to add.
    D (int): The number of chatting pairs in the classroom.
    chatting_pairs (list of tuples): A list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.

    Returns:
    (str, str): Two space-separated strings representing the optimal row and column indices for the aisles.

    The function works by counting the number of chatting pairs that can be separated by adding an aisle in each possible position.
    It then selects the most effective positions for aisles, aiming to separate as many chatting pairs as possible.

    Examples:
    - optimize_seating(4, 5, 1, 2, 3, [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)])
    Returns: ('2', '2 4')

    - optimize_seating(3, 3, 1, 1, 2, [(1, 2, 1, 3), (2, 1, 3, 1)])
    Returns: ('2', '2')
    """
    row_aisles = [0] * M
    column_aisles = [0] * N
    pairs_matrix = [[0]*N for _ in range(M)]

    for pair in chatting_pairs:
        pairs_matrix[pair[0]-1][pair[1]-1] += 1
        pairs_matrix[pair[2]-1][pair[3]-1] += 1

    for i in range(M):
        for j in range(N-1):
            pairs_matrix[i][j+1] += pairs_matrix[i][j]

    for i in range(M-1):
        for j in range(N):
            pairs_matrix[i+1][j] += pairs_matrix[i][j]

    for i in range(M):
        best = None
        for j in range(N):
            if pairs_matrix[i][j] < D/2:
                if best is None or pairs_matrix[i][j] > pairs_matrix[i][best]:
                    best = j
        if best is not None:
            column_aisles[best] += 1

    for j in range(N):
        best = None
        for i in range(M):
            if pairs_matrix[i][j] < D/2:
                if best is None or pairs_matrix[i][j] > pairs_matrix[best][j]:
                    best = i
        if best is not None:
            row_aisles[best] += 1

    row_aisles_str = " ".join([str(i+1) for i in range(M) if row_aisles[i] > 0])
    column_aisles_str = " ".join([str(i+1) for i in range(N) if column_aisles[i] > 0])

    return row_aisles_str, column_aisles_str
def test_optimize_seating():
    test_cases = [
        # Test case 1 from the provided example
        {
            'M': 4, 'N': 5, 'K': 1, 'L': 2, 'D': 3,
            'chatting_pairs': [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)],
            'expected': ('2', '2 4')
        },
        # Corrected Test case 2
        {
            'M': 5, 'N': 6, 'K': 2, 'L': 3, 'D': 4,
            'chatting_pairs': [(1, 1, 1, 2), (2, 2, 3, 2), (4, 5, 4, 6), (5, 1, 5, 2)],
            'expected': ('1 2', '1 2 5')  # Corrected expected output
        },
        # Test case 3
        {
            'M': 3, 'N': 3, 'K': 1, 'L': 1, 'D': 2,
            'chatting_pairs': [(1, 2, 1, 3), (2, 1, 3, 1)],
            'expected': ('2', '2')
        },
    ]

    for i, test in enumerate(test_cases, 1):
        row_output, col_output = optimize_seating(
            test['M'], test['N'], test['K'], test['L'], test['D'], test['chatting_pairs']
        )
        assert row_output == test['expected'][0], f"Test case {i} failed: row_output {row_output} does not match expected {test['expected'][0]}"
        assert col_output == test['expected'][1], f"Test case {i} failed: col_output {col_output} does not match expected {test['expected'][1]}"
        print(f"Test case {i} passed.")

# Run the test function
test_optimize_seating()