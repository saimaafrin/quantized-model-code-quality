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
    # Create a 2D matrix representing the classroom, where each entry represents the number of students between that position and (M+1, N+1).
    distance_matrix = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M + 1):
        for j in range(N + 1):
            distance_matrix[i][j] = abs(i - M) + abs(j - N)

    # Create a list of tuples representing the coordinates of the chatting pairs.
    chatting_pair_positions = [(i, j, p, q) for i, j, p, q in chatting_pairs]

    # Calculate the number of chatting pairs that can be separated by adding an aisle in each possible position.
    # This is done by counting the number of pairs that are within a certain distance of each aisle.
    # The aisles are placed in the form (row, column), with row and column indices ranging from 0 to M, N respectively.
    # The distance between an aisle and a chatting pair is calculated by the Euclidean distance formula.
    # The number of pairs that can be separated by an aisle is the number of pairs within that distance.
    # The number of pairs that can be separated by each aisle is then summed across all aisles to give a total number of pairs.
    total_separated_pairs = 0
    separated_pairs_by_aisle = [0] * K * L
    for aisle_index in range(K * L):
        aisle_row_index = aisle_index // L
        aisle_column_index = aisle_index % L
        for chatting_pair_index in range(D):
            chatting_pair_position = chatting_pair_positions[chatting_pair_index]
            distance = distance_matrix[chatting_pair_position[0]][chatting_pair_position[1]]
            if distance <= (M - aisle_row_index) + (N - aisle_column_index):
                separated_pairs_by_aisle[aisle_index] += 1
                total_separated_pairs += 1

    # Select the aisles that maximise the number of separated pairs.
    # This is done by sorting the separated pairs by aisle and then selecting the aisle with the highest number of separated pairs.
    # If two or more aisles have the same number of separated pairs, the first
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