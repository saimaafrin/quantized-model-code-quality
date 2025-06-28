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

    # Initialize a 2D array to store the number of ways
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # The only way to pass the ball to the starting student after 0 passes is to stay put
    for i in range(n + 1):
        dp[i][0] = 1

    # The only way to pass the ball to the starting student after 1 pass is to pass it to the left or right
    for i in range(2, m + 1):
        dp[1][i] = dp[2][i - 1] + dp[3][i - 1]
        for j in range(2, n + 1):
            dp[j][i] = dp[j - 1][i - 1] + dp[j + 1][i - 1]

    # The number of ways to pass the ball to the starting student after 'm' passes is the sum of the 
    # number of ways to pass the ball to the starting student after (m - 1) passes and the 
    # number of ways to pass the ball to the starting student after (m - 2) passes
    return sum([dp[1][i] for i in range(m + 1)])
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