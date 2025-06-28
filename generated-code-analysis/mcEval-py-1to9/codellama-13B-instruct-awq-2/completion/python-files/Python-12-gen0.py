def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    # Converting the number string into a list of digits
    digits = [int(digit) for digit in num_str]
    # Initializing the maximum product
    max_product = 0
    # Looping through all possible positions to insert the multiplication signs
    for i in range(N + K):
        # Initializing the product of the digits to the left of the current position
        left_product = 1
        # Looping through the digits to the left of the current position
        for j in range(i):
            # Multiplying the product of the digits to the left of the current position by the current digit
            left_product *= digits[j]
        # Initializing the product of the digits to the right of the current position
        right_product = 1
        # Looping through the digits to the right of the current position
        for j in range(i + 1, N):
            # Multiplying the product of the digits to the right of the current position by the current digit
            right_product *= digits[j]
        # Calculating the product of the digits to the left and right of the current position
        current_product = left_product * right_product
        # Updating the maximum product if the current product is greater
        max_product = max(max_product, current_product)
    # Returning the maximum product
    return max_product
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