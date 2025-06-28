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

    # Initialize variables
    aisle_row = [0] * K
    aisle_col = [0] * L
    chatting_pairs_separated = 0

    # For each chatting pair
    for pair in chatting_pairs:

        # Identify row and column indices for the pair
        row_1, col_1, row_2, col_2 = pair
        aisle_row_1 = aisle_col[row_1 - 1]
        aisle_col_1 = aisle_row[col_1 - 1]
        aisle_row_2 = aisle_col[row_2 - 1]
        aisle_col_2 = aisle_row[col_2 - 1]

        # If the chatting pair can be separated by an aisle
        if aisle_row_1 != row_2 and aisle_col_1 != col_2 and aisle_row_2 != row_1 and aisle_col_2 != col_1:
            chatting_pairs_separated += 1

    # If the chatting pairs cannot be separated
    if chatting_pairs_separated == 0:
        return " ".join(str(i) for i in aisle_row), " ".join(str(i) for i in aisle_col)

    # Initialize the list of valid aisle positions
    valid_aisle_positions = list(product(range(1, N + 1), range(1, M + 1)))

    # Initialize the list of aisle positions
    aisle_positions = []

    # While there are valid aisle positions
    while valid_aisle_positions:

        # Initialize the current best aisle position
        current_best_aisle_position = valid_aisle_positions.pop(0)

        # Initialize the current best number of chatting pairs separated
        current_best_chatting_pairs_separated = 0

        # For each aisle position
        for position in valid_aisle_positions:

            # If the current best aisle position and the current aisle position can separate more chatting pairs
            if count_chatting_pairs_separated(position, current_best_aisle_position, chatting_pairs) > current_best_chatting_pairs_separated:

                # Update the current best aisle position
                current_best_
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