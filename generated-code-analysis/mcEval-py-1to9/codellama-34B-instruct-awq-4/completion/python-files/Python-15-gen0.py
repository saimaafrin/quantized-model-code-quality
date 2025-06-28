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

    # Check the number of rows, columns, and chatting pairs are valid
    if M < 1 or N < 1 or K < 0 or L < 0 or D < 0:
        return ("Invalid input", "Invalid input")

    # Initialize the list of chatting pairs and the list of possible aisle positions
    chatting_pairs_list = []
    row_aisle_positions = list(range(1, M + 1))
    col_aisle_positions = list(range(1, N + 1))

    # Populate the list of chatting pairs
    for pair in chatting_pairs:
        chatting_pairs_list.append(pair)

    # Count the number of chatting pairs that can be separated by adding an aisle in each possible position
    row_counts = [0] * M
    col_counts = [0] * N
    for row_index in row_aisle_positions:
        for col_index in col_aisle_positions:
            row_count = 0
            col_count = 0
            for pair in chatting_pairs_list:
                if pair[0] < row_index and pair[1] < row_index:
                    row_count += 1
                if pair[2] < col_index and pair[3] < col_index:
                    col_count += 1
            row_counts[row_index - 1] += row_count
            col_counts[col_index - 1] += col_count

    # Remove the K most effective row positions for aisles
    for i in range(K):
        max_index = row_counts.index(max(row_counts))
        row_counts[max_index] = 0
        row_aisle_positions.remove(max_index + 1)

    # Remove the L most effective column positions for aisles
    for i in range(L):
        max_index = col_counts.index(max(col_counts))
        col_counts[max_index] = 0
        col_aisle_positions.remove(max_index + 1)

    # Return the optimized aisle positions
    row_aisle_positions.sort()
    row_aisle_positions = ' '.join(map(str, row_aisle_positions))
    col_aisle_positions.sort()
    col_aisle_positions = ' '.join(map
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