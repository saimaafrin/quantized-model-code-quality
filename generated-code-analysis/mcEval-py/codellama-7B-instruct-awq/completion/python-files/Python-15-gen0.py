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
    def get_dist(x, y):
        """
        Calculates the distance between two points on a grid.
        """
        return math.sqrt(pow((x - y), 2))

    def add_aisle(aisles, X, Y):
        """
        Adds an aisle at position X, Y and returns the updated list of aisles.
        """
        # Add the aisle to the list of aisles.
        aisles.append((X, Y))
        # Remove the aisle from the list of chatting pairs.
        for i, pair in enumerate(chatting_pairs):
            if X == pair[0] or Y == pair[1]:
                del chatting_pairs[i]
        return aisles

    def get_num_chatting_pairs(X, Y, aisles):
        """
        Returns the number of chatting pairs that can be separated by adding an aisle at position X, Y.
        """
        num_chatting_pairs = 0
        for pair in chatting_pairs:
            # Calculate the distance between the aisle and the chatting pair.
            dist_x = abs(X - pair[0])
            dist_y = abs(Y - pair[1])
            # If the distance is less than the distance to the next aisle, we can separate the chatting pair.
            if dist_x < get_dist(X, aisles[0][0]) or dist_y < get_dist(Y, aisles[0][1]):
                num_chatting_pairs += 1
        return num_chatting_pairs

    def get_max_chatting_pairs(X, Y):
        """
        Returns the number of chatting pairs that can be separated by adding an aisle at position X, Y.
        """
        # Initialize a list to hold the number of chatting pairs that can be separated.
        max_chatting_pairs = 0
        # Initialize a list of possible positions for the aisle.
        possible_positions = [(X, i) for i in range(1, N)]
        possible_positions.extend([(i, Y) for i in range(1, M)])
        for pos in possible_positions:
            # Add the aisle and update the number of chatting pairs that can be separated.
            aisles = add_aisle(aisles, X, Y)
            num_chatting_pairs = get_num_chatting_p
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