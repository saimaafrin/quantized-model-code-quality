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

    # Initialize a table to keep track of the number of ways to pass the ball
    # Each cell represents a student
    # If the cell is 1, it means the ball can pass from the previous student to the current student
    # If the cell is 0, it means the ball cannot pass from the previous student to the current student
    dp = [[0 for _ in range(m+1)] for _ in range(n)]
    dp[0][0] = 1

    # For each student, calculate the number of ways to pass the ball for 'm' times
    for i in range(1, n):
        dp[i][0] = 1
        for j in range(1, m+1):
            # The ball can pass from the previous student to the current student
            # or it can pass from the next student to the current student
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    # The number of ways to pass the ball for 'm' times is the sum of ways for 'm-1' times
    return dp[n-1][m]
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