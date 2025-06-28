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
    # Count the number of chatting pairs that can be separated by each possible aisle.
    # For each possible aisle (horizontal or vertical), a dictionary is used to store the number of chatting pairs that can be separated.
    # The dictionary keys are the aisle positions (row or column indices) and the values are the number of chatting pairs that can be separated.
    # The first dictionary is used to count horizontal aisles, the second dictionary is used to count vertical aisles.
    separated_by_horizontal_aisles = {}
    separated_by_vertical_aisles = {}
    for pair in chatting_pairs:
        x1, y1, x2, y2 = pair[0], pair[1], pair[2], pair[3]
        for row in range(1, M+1):
            if row == y1 or row == y2:
                continue
            for column in range(1, N+1):
                if column == x1 or column == x2:
                    continue
                if (row, column) in separated_by_horizontal_aisles:
                    separated_by_horizontal_aisles[(row, column)] += 1
                else:
                    separated_by_horizontal_aisles[(row, column)] = 1
        for column in range(1, N+1):
            if column == x1 or column == x2:
                continue
            for row in range(1, M+1):
                if row == y1 or row == y2:
                    continue
                if (row, column) in separated_by_vertical_aisles:
                    separated_by_vertical_aisles[(row, column)] += 1
                else:
                    separated_by_vertical_aisles[(row, column)] = 1
    # Select the aisle positions that can separate the most chatting pairs.
    # The selected aisle positions are stored in the lists 'horizontal_aisles' and 'vertical_aisles'.
    # If there is a tie, both aisle positions are selected.
    horizontal_aisles = []
    vertical_aisles = []
    for aisle in sorted(separated_by_horizontal_aisles.items(), key=lambda item: item[1], reverse=True):
        if len(horizontal_aisles) == K:
            break
        horizontal_aisles.append(str(aisle[0][0]))
    for aisle in sorted(separated_by_vertical_aisles.items(), key=lambda item: item[1], reverse=True):
        if len(vertical
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