def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    # initialize result
    res = 1

    # Count of numbers in num_str
    count = N

    # while count is greater than 0
    while count > 0:
        # find the maximum digit
        max_digit = max([int(num_str[i]) for i in range(count)])

        # find the maximum digit's index
        max_index = num_str.index(str(max_digit))

        # if maximum digit is not at the end
        if max_index != count - 1:
            # remove maximum digit from num_str
            num_str = num_str[:max_index] + num_str[max_index + 1:]

        # if K is greater than 0
        if K > 0:
            # if maximum digit is not at the start and the digit before it is not 1
            if max_index != 0 and num_str[max_index - 1] != '1':
                # insert '*' before maximum digit
                num_str = num_str[:max_index] + '*' + num_str[max_index:]
                # decrease K
                K -= 1
            # if maximum digit is at the start or the digit before it is 1
            else:
                # insert '*' after maximum digit
                num_str = num_str[:max_index + 1] + '*' + num_str[max_index + 1:]
                # decrease K
                K -= 1
        # if K is 0
        else:
            # insert '*' after maximum digit
            num_str = num_str[:max_index + 1] + '*' + num_str[max_index + 1:]

        # decrease count
        count -= 1

    # if K is not 0
    if K > 0:
        # insert '*' at the end
        num_str += '*'
        # decrease K
        K -= 1

    # calculate the product
    for i in num_str.split('*'):
        res *= int(i)

    # return the product
    return res
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