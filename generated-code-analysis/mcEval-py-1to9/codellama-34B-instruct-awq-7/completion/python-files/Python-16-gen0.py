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

    # Initialize an array with a single element to represent the state where 
    # there is only one student.
    dp = [1]

    # Populate the array with states representing a single student passing 
    # the ball to a neighbor.
    for i in range(1, m):
        dp.append(i)

    # Evaluate the state of passing the ball between n students.
    for i in range(m, n):
        # The number of distinct ways to pass the ball between i students is equal to the
        # sum of the number of distinct ways to pass the ball between the (i - 1) students
        # plus the number of ways to pass the ball between the (i - 2) students.
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n - 1]
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