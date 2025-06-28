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
    def count_chatting_pairs(x: int, y: int, horizontal: bool) -> int:
        """
        Count the number of chatting pairs that can be separated by an aisle at position (x, y).
        """
        count = 0
        for pair in chatting_pairs:
            if horizontal:
                if pair[0] == x and pair[2] == x and pair[1] < y < pair[3]:
                    count += 1
            else:
                if pair[1] == y and pair[3] == y and pair[0] < x < pair[2]:
                    count += 1
        return count

    # Count the number of chatting pairs that can be separated by each possible aisle
    counts = []
    for x in range(1, M):
        for y in range(1, N):
            counts.append((x, y, count_chatting_pairs(x, y, True), count_chatting_pairs(x, y, False)))

    # Sort the counts by the number of chatting pairs that can be separated
    counts.sort(key=lambda t: t[2] + t[3], reverse=True)

    # Select the positions for the aisles that maximize the number of chatting pairs that can be separated
    horizontal_aisles = [1]
    vertical_aisles = [1]
    for i in range(K + L):
        x, y, h_count, v_count = counts[i]
        if h_count > v_count:
            horizontal_aisles.append(y)
        else:
            vertical_aisles.append(x)

    # Sort the aisle positions and join them into strings
    horizontal_aisles.sort()
    vertical_aisles.sort()
    horizontal_aisles_str = ' '.join(map(str, horizontal_aisles))
    vertical_aisles_str = ' '.join(map(str, vertical_aisles))

    return horizontal_aisles_str, vertical_aisles_str
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