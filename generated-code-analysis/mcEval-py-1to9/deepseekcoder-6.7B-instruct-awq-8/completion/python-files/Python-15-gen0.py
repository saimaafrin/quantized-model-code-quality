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

    from collections import Counter

    # Count the number of chatting pairs in each row and column
    row_counts = Counter()
    col_counts = Counter()
    for (x1, y1, x2, y2) in chatting_pairs:
        if x1 == x2:
            row = x1
            for y in range(min(y1, y2), max(y1, y2) + 1):
                col_counts[(row, y)] += 1
        else:
            col = y1
            for x in range(min(x1, x2), max(x1, x2) + 1):
                row_counts[(x, col)] += 1

    # Add horizontal and vertical aisles
    for _ in range(K):
        # Find the row with the most chatting pairs
        row, _ = row_counts.most_common(1)[0][0]

        # Add an aisle in this row
        col_counts[row] += 1
        row_counts.pop(row)

        # Update counts for the affected rows and columns
        for col in range(1, N + 1):
            if (row, col) in col_counts:
                col_counts[(row - 1, col)] = col_counts[(row, col)]
                col_counts[(row, col)] = 0
        for r in range(1, M + 1):
            if (r, row) in row_counts:
                row_counts[(r, row - 1)] = row_counts[(r, row)]
                row_counts[(r, row)] = 0

    for _ in range(L):
        # Find the column with the most chatting pairs
        _, col = col_counts.most_common(1)[0][0]

        # Add an aisle in this column
        row_counts[col] += 1
        col_counts.pop(col)

        # Update counts for the affected rows and columns
        for row in range(1, M + 1):
            if (row, col) in row_counts:
                row_counts[(row - 1, col)] = row_counts[(row, col)]
                row_counts[(row, col)] = 0
        for c in range(1, N + 1):
            if (col, c) in col_counts:
                col_counts[(col - 1, c)] = col_counts[(col, c)]
                col_
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