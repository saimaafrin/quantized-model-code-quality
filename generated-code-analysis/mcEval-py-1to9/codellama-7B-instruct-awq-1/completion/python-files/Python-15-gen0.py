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

    # Compute the number of chatting pairs that can be separated by adding an aisle in each possible position.
    # Also, compute the number of chatting pairs that can be separated by adding an aisle in the first row.
    aisle_positions = [0, 0]
    row_aisle_count = 0
    for i in range(M):
        aisle_count = 0
        for j in range(N):
            aisle_count += is_chatting_pair(chatting_pairs, i, j)
        aisle_positions.append(aisle_count)
        row_aisle_count = max(row_aisle_count, aisle_count)

    # Compute the number of chatting pairs that can be separated by adding an aisle in the first column.
    col_aisle_count = 0
    for j in range(N):
        aisle_count = 0
        for i in range(M):
            aisle_count += is_chatting_pair(chatting_pairs, i, j)
        col_aisle_count = max(col_aisle_count, aisle_count)

    # Compute the number of chatting pairs that can be separated by adding an aisle in each possible position,
    # and select the most effective positions for aisles, aiming to separate as many chatting pairs as possible.
    best_row_index = 0
    best_col_index = 0
    best_row_count = 0
    best_col_count = 0
    for i in range(M):
        row_count = 0
        for j in range(N):
            row_count += is_chatting_pair(chatting_pairs, i, j)
        if row_count >= row_aisle_count:
            continue
        row_count += aisle_positions[i]
        if row_count > best_row_count:
            best_row_count = row_count
            best_row_index = i
    for j in range(N):
        col_count = 0
        for i in range(M):
            col_count += is_chatting_pair(chatting_pairs, i, j)
        if col_count >= col_aisle_count:
            continue
        col_count += aisle_positions[j]
        if col_count > best_col_count:
            best_col_count = col_count
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