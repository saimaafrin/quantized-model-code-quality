def count_passing_ways(n: int, m: int) -> int:
    """
    Counts the number of different ways to pass a ball among 'n' students arranged in a circle 
    such that after 'm' passes, the ball returns to the starting student.

    The function uses dynamic programming to determine the number of passing sequences. Each student
    can pass the ball either to the left neighbor or to the right neighbor.

    Args:
    n: The number of students standing in a circle.
    m: The number of times the ball is passed.

    Returns:
    An integer representing the number of distinct passing ways that result in the ball
    returning to the starting student after 'm' passes.

    Cases:
    >>> count_passing_ways(3, 3)
    2
    >>> count_passing_ways(5, 4)
    6
    """
    # Initialize the dynamic programming matrix with one row of size m + 1.
    # Each row contains the number of possible passing sequences for that particular
    # row index.
    dp = [[0] * (m + 1)]

    # Initialize the first row with the number of passing sequences for one pass
    # (from 0 to m)
    for i in range(m + 1):
        dp[0][i] = 1

    # For each row index from 2 to n
    for i in range(2, n + 1):

        # Add a new row to the dynamic programming matrix
        dp.append([0] * (m + 1))

        # For each column index from 0 to m
        for j in range(m + 1):

            # Determine the number of possible passing sequences for the current student
            if j < i:
                # If the current row index is less than the current column index,
                # the ball can only be passed to the right neighbor.
                dp[i - 1][j] = dp[i - 2][j - 1] + dp[i - 2][j]

            elif j >= i:
                # If the current row index is greater than or equal to the current column index,
                # the ball can only be passed to the left neighbor.
                dp[i - 1][j] = dp[i - 2][j - 1]

    return dp[n - 1][m]
def test_count_passing_ways():
    test_cases = [
        # Test case 1: simple case
        {
            'n': 3,
            'm': 1,
            'expected': 0
        },
        # Test case 2: another simple case
        {
            'n': 4,
            'm': 2,
            'expected': 2
        },
        # Test case 3: larger number of students and passes
        {
            'n': 5,
            'm': 3,
            'expected': 0
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = count_passing_ways(test['n'], test['m'])
        assert result == test['expected'], f"Test case {i} failed: result {result} does not match expected {test['expected']}"
        print(f"Test case {i} passed with result {result}.")

# Run the test function
test_count_passing_ways()