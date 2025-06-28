def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    numbers = [int(num) for num in num_str]
    dp = [[[-1 for _ in range(K + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

    def dfs(idx: int, mul: int, k: int) -> int:
        """
        Function name: dfs
        Arguments:
        idx (int): An integer representing the current index.
        mul (int): An integer representing the current multiplication.
        k (int): An integer representing the remaining number of multiplication signs.
        Return type: int
        """
        if k < 0:
            return -1
        if idx == N:
            return mul
        if dp[idx][mul][k] != -1:
            return dp[idx][mul][k]

        dp[idx][mul][k] = max(
            dfs(idx + 1, mul * numbers[idx], k - 1),
            dfs(idx + 1, mul, k),
            dfs(idx + 1, numbers[idx], k),
        )
        return dp[idx][mul][k]

    return dfs(0, 1, K)
def test_max_product():
    # Test case 1
    num_str1 = "123"
    N1 = 3
    K1 = 1
    expected_result1 = 36  # Corrected expected result: 1*23 = 23 or 12*3 = 36, max is 36
    assert max_product(num_str1, N1,
                       K1) == expected_result1, f"Test case 1 failed. Expected {expected_result1}, got {max_product(num_str1, N1, K1)}"

    # Test case 2
    num_str2 = "1234"
    N2 = 4
    K2 = 2
    expected_result2 = 144  # Corrected expected result: 1*2*34 = 68 or 12*3*4 = 144, max is 144
    assert max_product(num_str2, N2,
                       K2) == expected_result2, f"Test case 2 failed. Expected {expected_result2}, got {max_product(num_str2, N2, K2)}"

    # Test case 3
    num_str3 = "051"
    N3 = 3
    K3 = 1
    expected_result3 = 5  # 0*51 = 0 or 05*1 = 5, max is 5
    assert max_product(num_str3, N3,
                       K3) == expected_result3, f"Test case 3 failed. Expected {expected_result3}, got {max_product(num_str3, N3, K3)}"

    # If no assertion is raised, all test cases passed
    print("All test cases passed!")
test_max_product()