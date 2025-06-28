def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    if N <= 1 or K <= 0:
        return 1

    # dp[i] represents the maximum product that can be obtained by inserting K - i - 1 multiplication signs into the first i number digits.
    dp = [0] * (N + 1)
    # dp[0] = 1 represents the maximum product that can be obtained by inserting K - 0 - 1 multiplication signs into the first 0 number digits.
    dp[0] = 1

    for i in range(1, N + 1):
        # num_str[i] represents the i-th number digit in the number string.
        num = int(num_str[i])
        # If the number digit is smaller than the number of multiplication signs that can be inserted into it,
        # the maximum product is obtained by inserting K - i - 1 multiplication signs into the first i number digits.
        if num < K - i:
            dp[i] = dp[i - 1] * num
        else:
            # Otherwise, the maximum product is obtained by either inserting K - i - 1 multiplication signs into the first i number digits,
            # or by inserting K - i - 2 multiplication signs into the first i - 1 number digits and then multiplying the i-th number digit with the maximum product of the remaining number digits.
            dp[i] = max(dp[i - 1] * num, dp[i - 2] * num)

    return dp[N]
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