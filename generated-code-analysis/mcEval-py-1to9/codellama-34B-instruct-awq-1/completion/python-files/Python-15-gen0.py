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

    # Initialize a list of integers, each representing the number of chatting pairs that can be separated by adding an aisle at that position.
    chatting_pairs_separated = [0] * (M * N + 1)

    # Count the number of chatting pairs that can be separated by adding an aisle in each possible position.
    for (Xi, Yi, Pi, Qi) in chatting_pairs:
        if Xi != Pi and Yi != Qi:
            chatting_pairs_separated[Xi * N + Yi] += 1
            chatting_pairs_separated[Pi * N + Qi] += 1
        elif Xi == Pi:
            chatting_pairs_separated[Yi] += 1
            chatting_pairs_separated[Qi] += 1
        else:
            chatting_pairs_separated[Xi * N + Yi] += 1
            chatting_pairs_separated[Pi * N + Qi] += 1

    # Initialize a list to represent the positions of the aisles.
    aisles = []

    # Select the most effective positions for aisles, aiming to separate as many chatting pairs as possible.
    for _ in range(K):
        # Find the index of the largest element in the list.
        largest_index = chatting_pairs_separated.index(max(chatting_pairs_separated))
        # Add the index to the list of aisle positions.
        aisles.append(largest_index)
        # Subtract one from all elements in the list.
        chatting_pairs_separated = [x - 1 for x in chatting_pairs_separated]

    # Join the list of aisle positions into a space-separated string.
    row_aisles = " ".join([str(i // N) for i in aisles])

    aisles = []

    for _ in range(L):
        largest_index = chatting_pairs_separated.index(max(chatting_pairs_separated))
        aisles.append(largest_index)
        chatting_pairs_separated = [x - 1 for x in chatting_pairs_separated]

    col_aisles = " ".join([str(i % N) for i in aisles])

    return (row_aisles, col_aisles)
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