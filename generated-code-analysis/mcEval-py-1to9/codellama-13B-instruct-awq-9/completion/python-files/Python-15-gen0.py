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
    assert M > 0 and N > 0 and K > 0 and L > 0 and D > 0
    assert chatting_pairs is not None

    # Add aisles in every possible position
    aisles_h = [k for k in range(1, N + 1)]
    aisles_v = [l for l in range(1, M + 1)]

    # Initialize the counts for each position
    count_h = [0 for _ in range(len(aisles_h))]
    count_v = [0 for _ in range(len(aisles_v))]

    # Iterate over each chatting pair
    for pair in chatting_pairs:
        # Check if pair is separated by any aisle
        for i, h in enumerate(aisles_h):
            for j, v in enumerate(aisles_v):
                # If the pair is separated by an aisle, increment the count
                if pair[0] == h and pair[2] == h:
                    count_h[i] += 1
                if pair[1] == v and pair[3] == v:
                    count_v[j] += 1

    # Select the positions with the highest count and return them
    max_h = max(count_h)
    max_v = max(count_v)
    row_idx = aisles_v[count_v.index(max_v)] - 1
    col_idx = aisles_h[count_h.index(max_h)] - 1
    return f"{row_idx}", f"{col_idx} {' '.join([str(i) for i in aisles_h[count_h.index(max_h) + 1:]])}"
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