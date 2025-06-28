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
    # Convert the chatting pairs into a matrix of ones and zeros, with 1s indicating a chatting pair and 0s indicating no chatting pair
    chatting_pairs_matrix = [[0 for i in range(N)] for j in range(M)]
    for chatting_pair in chatting_pairs:
        row, col = chatting_pair[0], chatting_pair[1]
        chatting_pairs_matrix[row - 1][col - 1] = 1
        row, col = chatting_pair[2], chatting_pair[3]
        chatting_pairs_matrix[row - 1][col - 1] = 1

    # Iterate over all possible positions of aisles and count the number of chatting pairs that can be separated
    aisle_counts = []
    for row in range(M):
        for col in range(N):
            count = 0
            # Check if the cell is a chatting pair
            if chatting_pairs_matrix[row][col] == 1:
                # Check if the cell has an aisle to the left
                if row > 0 and col > 0 and chatting_pairs_matrix[row - 1][col - 1] == 1:
                    count += 1
                # Check if the cell has an aisle to the right
                if row > 0 and col < (N - 1) and chatting_pairs_matrix[row - 1][col + 1] == 1:
                    count += 1
                # Check if the cell has an aisle below
                if col > 0 and chatting_pairs_matrix[row][col - 1] == 1:
                    count += 1
                # Check if the cell has an aisle above
                if col < (N - 1) and chatting_pairs_matrix[row][col + 1] == 1:
                    count += 1
            aisle_counts.append(count)
    # Sort the aisle counts in descending order to find the optimal positions of aisles
    aisle_counts.sort(reverse=True)
    # Select the K most effective aisle positions
    aisle_positions = [i + 1 for i in range(K) if aisle_counts[i] != 0]
    aisle_positions.sort()
    # Convert the positions of aisles into a row and column index
    rows_string = " ".join(
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