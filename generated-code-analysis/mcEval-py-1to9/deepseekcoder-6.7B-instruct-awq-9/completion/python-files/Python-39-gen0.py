def calculate_arrangements(n, m, a) -> int:
    """
    Compute the number of ways to arrange m pots of flowers using up to n types,
    where the ith type can have at most a[i] pots, and the arrangement must be in
    increasing order of flower types.

    Args:
    - n (int): The number of flower types available.
    - m (int): The total number of flower pots to arrange.
    - a (list of int): A list where a[i] is the maximum number of pots for the ith type of flower.

    Returns:
    - int: The number of distinct arrangements modulo (10^6 + 7).

    Examples:
    - calculate_arrangements(2, 4, [3, 2]) returns 2.
    - calculate_arrangements(3, 3, [1, 2, 3]) returns 6.
    """

    MOD = 10**6 + 7
    fact = [1]
    inv = [1]
    inv_fact = [1]
    for i in range(1, m + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((MOD - MOD // i) * inv[MOD % i] % MOD)
        inv_fact.append((inv_fact[-1] * inv[i]) % MOD)

    dp = [0] * (m + 1)
    dp[0] = 1

    for i in range(n):
        dp_new = dp[:]
        for j in range(m, a[i] - 1, -1):
            dp_new[j] = 0
            for k in range(1, min(j, a[i]) + 1):
                dp_new[j] = (dp_new[j] + dp[j - k] * fact[k] * inv_fact[k - 1] % MOD)
        dp = dp_new

    return dp[m]
def test_calculate_arrangements():
    # Helper function to compare expected and actual results
    def assert_equal(actual, expected, message):
        assert actual == expected, message

    # Test Case 1
    n, m, a = 2, 4, [3, 2]
    expected = 2
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 1 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 2
    n, m, a = 3, 3, [1, 2, 3]
    expected = 6
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 2 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 3
    n, m, a = 1, 5, [5]
    expected = 1
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 3 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    print("All tests passed!")

if __name__ == "__main__":
    test_calculate_arrangements()