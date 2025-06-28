def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    assert (1 <= N <= 10)
    assert (0 <= K <= N)

    # convert number string to integer list for calculation
    nums = list(map(int, num_str))

    # calculate the product of all numbers in nums
    total_product = 1
    for num in nums:
        total_product *= num

    # calculate the maximum product by calculating the product of all numbers in nums
    # except for one part that is the product of all numbers in the current segment
    # the segment length is determined by K
    max_product = 0
    for segment_length in range(1, N+1):
        if segment_length <= K+1:
            segment_product = 1
            for num in nums[:segment_length]:
                segment_product *= num
            for num in nums[segment_length:segment_length+K+1]:
                segment_product //= num
            max_product = max(max_product, segment_product)
        else:
            break

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