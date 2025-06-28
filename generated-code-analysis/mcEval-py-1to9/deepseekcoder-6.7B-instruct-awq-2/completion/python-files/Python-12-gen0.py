def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    # This is a recursive function that calculates the maximum product of the
    # substrings of num_str by inserting K multiplication signs.
    def max_product_rec(num_str: str, K: int) -> int:
        # If all the multiplication signs are inserted, calculate the product of
        # the whole number string and return it.
        if K == 0:
            return int(num_str)
        # If the string is too short to insert a multiplication sign, return 0.
        if len(num_str) <= K + 1:
            return 0
        # Calculate the product of the substrings and the remaining substrings by
        # inserting a multiplication sign.
        max_val = 0
        for i in range(1, len(num_str)):
            # Calculate the product of the current substring and the remaining
            # substrings by inserting K - 1 multiplication signs.
            cur = int(num_str[:i]) * max_product_rec(num_str[i:], K - 1)
            # Update the maximum value.
            if cur > max_val:
                max_val = cur
        # Return the maximum value.
        return max_val

    # Call the recursive function and return the result.
    return max_product_rec(num_str, K)
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