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
    from collections import defaultdict

    # Count the number of chatting pairs for each possible aisle position
    row_aisles = defaultdict(int)
    col_aisles = defaultdict(int)
    for pair in chatting_pairs:
        x1, y1, x2, y2 = pair
        if x1 == x2:
            row_aisles[(x1, min(y1, y2), max(y1, y2))] += 1
        else:
            col_aisles[(min(x1, x2), y1, max(x1, x2))] += 1

    # Add the aisles
    row_aisles_list = sorted(list(row_aisles.items()), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))
    col_aisles_list = sorted(list(col_aisles.items()), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))

    # If there are not enough aisles, add them all
    if len(row_aisles_list) < K:
        K = len(row_aisles_list)
    if len(col_aisles_list) < L:
        L = len(col_aisles_list)

    # Get the indices of the optimal aisles
    row_aisles_indices = [str(row_aisles_list[i][0][0]) for i in range(K)]
    col_aisles_indices = [str(col_aisles_list[i][0][0]) for i in range(L)]

    return ' '.join(row_aisles_indices), ' '.join(col_aisles_indices)
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