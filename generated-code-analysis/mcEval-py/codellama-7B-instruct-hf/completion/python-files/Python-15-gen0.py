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
    # Compute the number of chatting pairs that can be separated by adding an aisle in each possible position
    # The number of chatting pairs that can be separated is stored in a list where the position of the aisle is the index
    # For example, if a row of aisles is added, the number of chatting pairs that can be separated is stored in aisles_rows[i]
    # where i is the index of the row of aisles
    aisles_rows = [0] * M
    aisles_cols = [0] * N
    for (x, y, p, q) in chatting_pairs:
        if x in range(M):
            aisles_rows[x] += 1
        if y in range(N):
            aisles_cols[y] += 1
    for (x, y, p, q) in chatting_pairs:
        if x in range(M) and y in range(N):
            aisles_rows[x] += 1
            aisles_cols[y] += 1

    # Count the number of aisles that are already in place
    n_aisles_rows = 0
    n_aisles_cols = 0
    for i in range(M):
        for j in range(N):
            if aisles_rows[i] > 0 and aisles_cols[j] > 0:
                n_aisles_rows += 1
                n_aisles_cols += 1
                aisles_rows[i] -= 1
                aisles_cols[j] -= 1

    # The function optimizes the placement of aisles by trying to separate as many chatting pairs as possible
    # The first aisle that separates a chatting pair is chosen
    # The function continues iterating over the chatting pairs until all pairs have been processed
    # The final result is the position of the aisle that resulted in the highest separation of chatting pairs
    max_separation = 0
    max_aisles = []
    for (x, y, p, q) in chatting_pairs:
        if x in range(M) and y in range(N) and aisles_rows[x] > 0 and aisles_cols[y] > 0:
            aisles_rows[x] -= 1
            aisles_cols[y] -= 1
            separation = aisles_rows[x] + aisles_cols[y] - 1
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