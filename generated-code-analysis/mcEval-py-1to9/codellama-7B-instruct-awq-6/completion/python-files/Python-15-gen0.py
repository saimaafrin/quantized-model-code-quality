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

    # Add vertical and horizontal aisles, and count the number of chatting pairs that can be separated.
    vertical_aisles = [[0 for _ in range(N)] for _ in range(M)]
    horizontal_aisles = [[0 for _ in range(M)] for _ in range(N)]
    chatting_pairs_separated = 0

    for pair in chatting_pairs:
        # Check if the chatting pair can be separated by an aisle.
        if pair[0] in range(M) and pair[1] in range(N):
            vertical_aisles[pair[0]][pair[1]] = 1
            horizontal_aisles[pair[0]][pair[1]] = 1
            chatting_pairs_separated += 1

    # Count the number of chatting pairs that can be separated by adding an aisle in each possible position.
    rows_chatting_separated = 0
    cols_chatting_separated = 0

    # Horizontal aisles.
    for row in range(M):
        for col in range(N):
            # Check if the aisle can be added.
            if vertical_aisles[row][col] == 1:
                # Add the aisle and separate the chatting pairs.
                vertical_aisles[row][col] = 0
                horizontal_aisles[row][col] = 0
                rows_chatting_separated += 1

    # Vertical aisles.
    for row in range(M):
        for col in range(N):
            # Check if the aisle can be added.
            if horizontal_aisles[row][col] == 1:
                # Add the aisle and separate the chatting pairs.
                vertical_aisles[row][col] = 0
                horizontal_aisles[row][col] = 0
                cols_chatting_separated += 1

    # Select the most effective positions for aisles.
    rows = ''
    cols = ''
    max_separated_pairs = max(rows_chatting_separated, cols_chatting_separated)

    if rows_chatting_separated == max_separated_pairs:
        for row in range(M):
            for col in range(N):
                # Check if an aisle can be added.
                if vertical_aisles[row][col] == 1:
                    rows += str(row) + ' '

    if cols_chatting_
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