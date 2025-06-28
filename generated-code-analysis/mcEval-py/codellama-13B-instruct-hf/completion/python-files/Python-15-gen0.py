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
    # Initialize variables and lists
    row_indices = list(range(M))
    col_indices = list(range(N))
    num_chatting_pairs = D
    optimal_row_indices = []
    optimal_col_indices = []

    # Calculate the number of chatting pairs that can be separated by adding an aisle in each possible position
    for row_index in row_indices:
        for col_index in col_indices:
            # Initialize aisle counter
            aisle_counter = 0
            for pair in chatting_pairs:
                # If the chatting pair is not separated by an aisle, count it
                if (pair[0] not in optimal_row_indices) and (pair[1] not in optimal_col_indices):
                    aisle_counter += 1

            # If the current position is the most effective, update the optimal row and col indices
            if aisle_counter == num_chatting_pairs:
                optimal_row_indices = [row_index]
                optimal_col_indices = [col_index]

    # If there are still multiple effective positions, iterate through them to find the most efficient combination
    if len(optimal_row_indices) > 1:
        for row_index in row_indices:
            for col_index in col_indices:
                # If the current position is the most effective, update the optimal row and col indices
                if (row_index not in optimal_row_indices) and (col_index not in optimal_col_indices):
                    optimal_row_indices.append(row_index)
                    optimal_col_indices.append(col_index)

    # Return the optimal row and col indices
    return " ".join(str(index) for index in optimal_row_indices), " ".join(str(index) for index in optimal_col_indices)
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