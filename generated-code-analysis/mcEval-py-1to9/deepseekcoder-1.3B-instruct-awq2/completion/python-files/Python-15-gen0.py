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
    from itertools import combinations
    from operator import itemgetter

    # Ensure the aisles are evenly distributed.
    K = K * 2 if K % 2 == 0 else K * 2 + 1
    L = L * 2 if L % 2 == 0 else L * 2 + 1

    # Calculate the total number of possible aisles.
    total_aisles = M * N

    # Calculate the total number of chatting pairs.
    total_pairs = len(chatting_pairs)

    # Calculate the number of chatting pairs that can be separated by adding an aisle.
    # Assume that the aisles are placed in the center.
    valid_pairs = [(x, y) for (x, y, p, q) in chatting_pairs if max(x, y) - min(p, q) <= K and min(x, y) - max(p, q) <= L]

    # Sort the chatting pairs by their maximum distance.
    valid_pairs.sort(key=itemgetter(max), reverse=True)

    # Choose the most effective positions for aisles.
    aisle_positions = [(x, y) for (x, y, p, q) in chatting_pairs if (x, y) not in valid_pairs]
    aisle_positions.sort(key=itemgetter(0))

    # Calculate the number of aisles placed in each position.
    aisle_counts = [(x, y) for (x, y) in combinations(range(M), aisle_positions[0][0]+K) for (y, x) in combinations(range(N), aisle_positions[0][1]+L) if (x, y) in aisle_positions]

    # Sort the aisles by the number of chatting pairs they can be placed in.
    aisle_counts.sort(key=itemgetter(1), reverse=True)

    return str(aisle_positions[0][0]) + ' ' + str(aisle

print(optimize_seating(4, 5, 1, 2, 3, [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)]))
print(optimize_seating(3, 3, 1, 1, 2, [(1, 2, 1, 3), (2,
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