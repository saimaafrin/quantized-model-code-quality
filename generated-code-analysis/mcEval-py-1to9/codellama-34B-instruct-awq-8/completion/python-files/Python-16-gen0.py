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

    # Initialize a 2D array with rows and columns representing students.
    dp = [[0] * m for _ in range(n)]

    # The ball can only start moving from the first student.
    dp[0][0] = 1

    # The first student can only pass the ball to the left neighbor or the right neighbor.
    dp[1][0] = 1

    # Set the number of passes to 2, so that the ball can move.
    passes = 2

    # Loop through all students starting from the third one.
    for i in range(2, n):
        for j in range(m):
            # The current student can receive the ball only if the previous student has passed it.
            if j - passes >= 0:
                dp[i][j] = dp[i - 1][j - passes]

            # The current student can also receive the ball if the previous student's left neighbor
            # has passed it to the current student.
            if j - passes - 1 >= 0:
                dp[i][j] += dp[i - 2][j - passes - 1]

        # Increment the number of passes.
        passes += 1

    return dp[n - 1][m - 1]
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