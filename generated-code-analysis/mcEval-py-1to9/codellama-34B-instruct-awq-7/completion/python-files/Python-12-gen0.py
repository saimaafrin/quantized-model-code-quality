def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """

    def maximum_product(num_str: str, N: int, K: int, sign: int) -> int:
        """
        Function name: maximum_product
        Arguments:
        num_str (str): A string representing the number string.
        N (int): An integer representing the length of the number string.
        K (int): An integer representing the number of multiplication signs to insert.
        sign (int): An integer representing the index of the last multiplication sign.
        Return type: int (The function returns the maximum product that can be obtained by inserting K multiplication signs into the number string.)
        """
        if K == 0:
            # Base case
            # Calculate the product of the number string
            product = 1
            for i in range(N):
                product *= int(num_str[i])
            return product
        if sign == N:
            # Base case
            # Calculate the product of the number string
            product = 1
            for i in range(N):
                product *= int(num_str[i])
            return product
        if num_str[sign] == "0":
            # If the last number is 0, then the product will be 0
            return 0

        max_product = -1

        # Calculate the maximum product
        # Insert a multiplication sign at the index sign
        # Recursively calculate the maximum product for K - 1 multiplication signs
        for i in range(sign + 1, N):
            if num_str[i] == "0":
                continue
            product = int(num_str[sign]) * int(num_str[i])
            temp = maximum_product(num_str, N, K - 1, i)
            product *= temp
            max_product = max(max_product, product)
        return max_product

    # Initialize the maximum product
    max_product = -1

    # Iterate over all indices
    # Recursively calculate the maximum product for K multiplication signs at each index
    for i in range(N):
        product = maximum_product(num_str, N, K, i)
        max_product = max(max_product, product)
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