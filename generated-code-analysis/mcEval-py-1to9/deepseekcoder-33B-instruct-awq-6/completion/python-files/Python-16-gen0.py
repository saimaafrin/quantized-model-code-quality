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
    # Initialize a 2D table to store intermediate results
    dp = [[0]*n for _ in range(n)]

    # Initialize the table for 1 pass
    for i in range(n):
        dp[i][i] = 1
        dp[i][(i-1)%n] = 1

    # Populate the table for m passes
    for _ in range(m-1):
        new_dp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_dp[i][j] = dp[i][(j-1)%n] + dp[i][(j+1)%n]
        dp = new_dp

    # The total number of ways is the sum of the ways for each starting student
    return sum(dp[i][(i-1)%n] for i in range(n))
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