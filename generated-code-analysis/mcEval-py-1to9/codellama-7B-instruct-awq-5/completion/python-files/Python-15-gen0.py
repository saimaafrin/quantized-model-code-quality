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

    # Create a matrix of -1s with dimensions of N x M
    matrix = [[-1 for i in range(N)] for j in range(M)]

    # Inserts the chatting pairs into the matrix
    for pair in chatting_pairs:
        # Assigns a value of 1 to each cell of the chatting pair
        for i in range(pair[0][0], pair[0][1]):
            for j in range(pair[1][0], pair[1][1]):
                matrix[i][j] = 1

    # Calculates the chatting pairs after each aisle is inserted
    chatting_pairs_after_aisle = [0] * len(chatting_pairs)
    for i in range(0, len(chatting_pairs)):
        chatting_pairs_after_aisle[i] = count_chatting_pairs(matrix)

    # Finds the most effective positions for the aisles
    aisle_positions = []
    aisle_locations = []
    for i in range(0, len(chatting_pairs)):
        chatting_pairs_after_aisle[i] = chatting_pairs_after_aisle[i] - count_chatting_pairs(matrix)

        if chatting_pairs_after_aisle[i] > 0:
            aisle_positions.append(i)

    # Sorts the aisle positions based on the number of chatting pairs separated
    aisle_positions.sort(key=lambda x: chatting_pairs_after_aisle[x], reverse=True)

    # Selects the most effective positions for the aisles
    aisle_positions = aisle_positions[:K + L]

    # Calculates the chatting pairs after each aisle is inserted
    chatting_pairs_after_aisle = [0] * len(chatting_pairs)
    for i in range(0, len(chatting_pairs)):
        chatting_pairs_after_aisle[i] = count_chatting_pairs(matrix)

    # Inserts an aisle at each selected position
    for i in range(0, len(aisle_positions)):
        aisle_row = aisle_positions[i]
        aisle_column = chatting_pairs[aisle_row][0]

        # Inserts a vertical aisle
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