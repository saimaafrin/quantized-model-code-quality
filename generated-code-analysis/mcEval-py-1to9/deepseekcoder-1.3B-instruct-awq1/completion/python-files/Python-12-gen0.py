def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """

    def insert_signs(num_str: str, N: int, K: int) -> str:
        """
        A helper function that inserts multiplication signs into the number string.
        """

        multiplier = 1
        result = ''
        count = 0
        for i in range(N):
            if num_str[i] != '0' or i == N - 1:
                result += num_str[i]
                if count % 2 == 0:
                    result += '*' * multiplier
                    multiplier = 1
                else:
                    multiplier *= int(num_str[i])
            count += 1
        return result

    num_str = num_str.replace('+', '').replace('-', '')
    left = insert_signs(num_str[:N//2], N//2, K)
    right = insert_signs(num_str[N//2:], N//2, K)
    left_negative = '-' + left if num_str[0] != '-' else left
    right_negative = '-' + right if num_str[N//2] != '-' else right
    return max(int(left_negative), int(right_negative))
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