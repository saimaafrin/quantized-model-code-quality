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
    # Initialize the chatting graph with K + 1 horizontal edges and L + 1 vertical edges
    graph = [[K + 1] * (N + 1) for _ in range(M + 1)]

    # Update the chatting graph to reflect the presence of chatting pairs
    for chatting_pair in chatting_pairs:
        # Get the positions of the chatting pair
        Xi, Yi, Pi, Qi = chatting_pair

        # Compute the number of horizontal and vertical aisles needed to separate the chatting pair
        horizontal_aisles = Pi - Xi
        vertical_aisles = Qi - Yi

        # Add a horizontal edge to the chatting graph if the chatting pair can be separated by a horizontal aisle
        if horizontal_aisles > 0:
            graph[Xi][Yi] += 1
            graph[Pi][Qi] += 1

        # Add a vertical edge to the chatting graph if the chatting pair can be separated by a vertical aisle
        if vertical_aisles > 0:
            graph[Xi][Yi] += 1
            graph[Pi][Qi] += 1

    # Set the diagonal edges of the chatting graph to 0
    for i in range(M + 1):
        graph[i][i] = 0

    # Get the maximum flow in the chatting graph
    max_flow = max(graph, key=lambda row: max(row))

    # Initialize the row and column indices of the most effective aisles
    row_indices = []
    column_indices = []

    # Loop over the rows in the chatting graph
    for i in range(M + 1):
        # Get the current row of the chatting graph
        row = graph[i]

        # Loop over the indices in the current row
        for j in range(N + 1):
            # Check if the current index has the maximum flow in the chatting graph
            if row[j] == max_flow:
                # Add the row and column indices to the list of most effective aisles
                row_indices.append(i + 1)
                column_indices.append(j + 1)

    # Sort the row and column indices in ascending order
    row_indices.sort()
    column_indices.sort()

    # Convert the row and column indices to strings
    row_indices_string = ' '.join(map(str, row_indices))
    column_indices_string
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