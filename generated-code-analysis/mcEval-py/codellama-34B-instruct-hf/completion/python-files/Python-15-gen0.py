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
    rows_num = M - K
    cols_num = N - L
    assert rows_num > 0 and cols_num > 0, "The classroom must have at least 1 row and 1 column."

    chatting_pairs.sort(key=lambda x: x[0])
    chatting_pairs.sort(key=lambda x: x[1])
    aisle_rows = [0] * rows_num
    aisle_cols = [0] * cols_num
    for i in range(K):
        aisle_rows[i] = i
    for i in range(L):
        aisle_cols[i] = i

    count_of_seperated = D
    best_seperated_aisle_rows = [0] * K
    best_seperated_aisle_cols = [0] * L
    for _ in range(K * L):
        cur_seperated = count_of_seperated
        for i in range(K):
            cur_aisle_row = aisle_rows[i]
            for j in range(L):
                cur_aisle_col = aisle_cols[j]
                for pair in chatting_pairs:
                    if (
                        pair[0] <= cur_aisle_row < pair[1]
                        or pair[1] <= cur_aisle_row < pair[0]
                    ) and (
                        pair[2] <= cur_aisle_col < pair[3]
                        or pair[3] <= cur_aisle_col < pair[2]
                    ):
                        count_of_seperated -= 1
                        break
                if count_of_seperated < cur_seperated:
                    cur_seperated = count_of_seperated
                    best_seperated_aisle_rows = [0] * K
                    best_seperated_aisle_cols = [0] * L
                    best_seperated_aisle_rows[i] = cur_aisle_row
                    best_seperated_aisle_cols[j] = cur_aisle_col
        if cur_seperated == count_of_seperated:
            break

    return " ".join(str(x) for x in best_seperated_aisle_rows), " ".join(str(x) for x in best_seperated_aisle_cols)
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