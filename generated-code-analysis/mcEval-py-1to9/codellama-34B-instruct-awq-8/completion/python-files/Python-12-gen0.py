def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    # Initialize a dictionary to store the maximum product for a given string.
    dp = {}
    # Initialize a dictionary to store the minimum product for a given string.
    dp_min = {}

    # Initialize the maximum product for an empty string.
    dp[""] = 1
    # Initialize the minimum product for an empty string.
    dp_min[""] = 1

    # Loop for each digit in the number string.
    for i in range(N):
        # Initialize a string to store the current digit.
        cur = str(num_str[i])
        # Loop for each length of the multiplication signs.
        for j in range(1, K + 1):
            # Initialize a string to store the previous digit.
            prev = str(num_str[i - j])
            # Check if the current digit is not 0.
            if cur != "0":
                # Update the maximum product.
                dp[cur + prev] = max(
                    dp[cur + prev], int(cur + prev), dp[cur] * int(prev)
                )
                # Update the minimum product.
                dp_min[cur + prev] = min(
                    dp_min[cur + prev], int(cur + prev), dp_min[cur] * int(prev)
                )
            # Check if the previous digit is not 0.
            if prev != "0":
                # Update the maximum product.
                dp[prev + cur] = max(
                    dp[prev + cur], int(prev + cur), dp[prev] * int(cur)
                )
                # Update the minimum product.
                dp_min[prev + cur] = min(
                    dp_min[prev + cur], int(prev + cur), dp_min[prev] * int(cur)
                )

    # Return the maximum product.
    return dp[num_str[N - 1 ::]]
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