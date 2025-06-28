def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """

    """
    Functionality:
    The function max_product is designed to find the maximum product of a number string after inserting a certain number of multiplication signs.

    It accomplishes this by using a dynamic programming approach. It starts by creating a 2D table, dp, where dp[i][j] represents the maximum product that can be obtained by inserting j multiplication signs into the first i digits of the number string.

    Next, the function fills up the dp table iteratively. For each cell in the table, it calculates the maximum product by considering different possible ways to insert multiplication signs.

    After filling up the table, the function returns the maximum product, which is stored in dp[N][K], as the maximum product for the entire number string.
    """

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = dp[i-1][j] * int(num_str[i-1])
            for k in range(1, j+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-k] * int(num_str[i-1]))

    return dp[N][K]
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