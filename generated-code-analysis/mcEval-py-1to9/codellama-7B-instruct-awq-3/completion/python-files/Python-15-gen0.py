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
    num_chatting_pairs = D

    # This matrix counts the number of pairs of students in each row and column (with a value of 0 if the pair isn't in the classroom).
    # It is also used to determine if a row or column is entirely covered by chatting pairs (indicating that an aisle is not needed there).
    chatting_pairs_matrix = [[0] * N for _ in range(M)]

    for i in range(D):
        chatting_pairs_matrix[chatting_pairs[i][0]][chatting_pairs[i][1]] += 1
        chatting_pairs_matrix[chatting_pairs[i][2]][chatting_pairs[i][3]] += 1

    chatting_pairs_row_count = [[0] * N for _ in range(M)]
    chatting_pairs_col_count = [[0] * M for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if chatting_pairs_matrix[i][j] > 0:
                chatting_pairs_row_count[i][j] = 1
                chatting_pairs_col_count[j][i] = 1

    # This list counts the number of chatting pairs in each possible row.
    # It is used to determine the most effective positions for aisles.
    row_chatting_pairs = []
    for i in range(M):
        row_chatting_pairs.append(0)
        for j in range(N):
            row_chatting_pairs[i] += chatting_pairs_row_count[i][j]

    # This list counts the number of chatting pairs in each possible column.
    # It is used to determine the most effective positions for aisles.
    col_chatting_pairs = []
    for i in range(N):
        col_chatting_pairs.append(0)
        for j in range(M):
            col_chatting_pairs[i] += chatting_pairs_col_count[j][i]

    # This list counts the number of chatting pairs in each possible row and column.
    # It is used to determine the most effective positions for aisles.
    row_col_chatting_pairs = []
    for i in range(M):
        row_col_chatting_pairs.append([])
        for j in range(N):
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