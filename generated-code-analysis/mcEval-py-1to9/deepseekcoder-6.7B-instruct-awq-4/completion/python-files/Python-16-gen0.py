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

    # Dynamic programming table to store the number of passing sequences.
    dp = [[0]*m for _ in range(n)]

    # Initialize the dp table for the base case where there is only one student.
    dp[0][0] = 1

    # Iterate over each student from 1 to n.
    for i in range(1, n):
        # Iterate over each pass from 1 to m.
        for j in range(m):
            # The number of passing sequences for the current student and pass is the sum of the
            # number of passing sequences for the previous student and pass and the previous student
            # and the same pass minus one.
            dp[i][j] = dp[i-1][j] + dp[(i-1)%n][(j-1)%m]

    # Return the number of passing sequences for the last student and the last pass.
    return dp[-1][-1]
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