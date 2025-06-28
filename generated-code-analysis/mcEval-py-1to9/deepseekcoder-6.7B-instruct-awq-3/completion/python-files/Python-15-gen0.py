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
    # Calculate the initial number of chatting pairs that can be separated by aisles
    chatting_count = sum(1 for (x1, y1, x2, y2) in chatting_pairs if (x1, y1) == (x2, y2))

    # Calculate the counts of chatting pairs that can be separated by aisles in each position for rows and columns
    row_counts = [0] * (M + K + 1)
    col_counts = [0] * (N + L + 1)
    for (x1, y1, x2, y2) in chatting_pairs:
        if x1 == x2 and y1 < y2 and y2 - y1 == K + 1:  # Vertical chatting pair
            row_counts[x1] += 1
        if y1 == y2 and x1 < x2 and x2 - x1 == L + 1:  # Horizontal chatting pair
            col_counts[y1] += 1

    # Calculate the counts of chatting pairs that can be separated by aisles in each position for rows and columns
    for i in range(1, M + K + 1):
        row_counts[i] += row_counts[i - 1]
    for i in range(1, N + L + 1):
        col_counts[i] += col_counts[i - 1]

    # Calculate the counts of chatting pairs that can be separated by aisles by adding aisles in each position
    row_counts_with_aisles = [row_counts[i] - row_counts[max(0, i - K - 1)] for i in range(M + K + 1)]
    col_counts_with_aisles = [col_counts[i] - col_counts[max(0, i - L - 1)] for i in range(N + L + 1)]

    # Select the positions for the aisles to maximize the count of chatting pairs
    max_chatting_count = chatting_count
    max_row_positions = [0]
    max_col_positions = [0]
    for row_position in range(1, M + K + 1):
        for col_position in range(1, N + L + 1):
            new_chatting_count = chatting_count
            new_chatting_count += row_counts_with_aisles[row_position]
            new_chatting_count += col_counts_with_ais
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