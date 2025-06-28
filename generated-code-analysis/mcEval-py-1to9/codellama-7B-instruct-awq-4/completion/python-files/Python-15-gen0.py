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

    def get_chatting_pairs(a: int, b: int, c: int, d: int) -> list:
        """
        Return a list of chatting pairs that can be separated by an aisle in a given position.

        Args:
        a (int): The column index of the left edge of the aisle.
        b (int): The column index of the right edge of the aisle.
        c (int): The row index of the upper edge of the aisle.
        d (int): The row index of the lower edge of the aisle.

        Returns:
        list: A list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.

        The function works by counting the number of chatting pairs that can be separated by adding an aisle in a given position.
        It returns a list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.
        """
        chatting_pairs_in_aisle = []
        for chatting_pair in chatting_pairs:
            if (a <= chatting_pair[0] <= b and c <= chatting_pair[1] <= d) or (a <= chatting_pair[2] <= b and c <= chatting_pair[3] <= d) or (a <= chatting_pair[4] <= b and c <= chatting_pair[5] <= d) or (a <= chatting_pair[6] <= b and c <= chatting_pair[7] <= d):
                chatting_pairs_in_aisle.append(chatting_pair)
        return chatting_pairs_in_aisle

    def get_max_chatting_pairs_separated(chatting_pairs_in_aisle: list) -> int:
        """
        Return the maximum number of chatting pairs that can be separated by an aisle.

        Args:
        chatting_pairs_in_aisle (list): A list of chatting pairs that can be separated by an aisle in a given position.

        Returns:
        int: The maximum number of chatting pairs that can be separated by an aisle in a given position.

        The function works by counting the number of chatting pairs that can be separated by adding an aisle in a given position.
        It returns the maximum number of chatting pairs that can be separated by an aisle in a given position.
        """
        max_chatting
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