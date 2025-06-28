def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """

    # WRITE YOUR CODE HERE

    if K == 0:
        return 0

    # Create two lists to store the multiplication signs
    prefix = []
    suffix = []

    # Create a list to store the numbers
    nums = []

    # Iterate through the string and split it into numbers
    for i in range(N):
        nums.append(int(num_str[i]))

    # Iterate through the numbers and insert multiplication signs
    # If the current number is not the last number, insert a multiplication sign
    for i in range(N - 1):
        if i == 0:
            prefix.append(nums[0])
        else:
            prefix.append(prefix[i - 1] * nums[i])

        if i != N - 2:
            suffix.append(nums[i + 1])
        else:
            suffix.append(nums[i + 1])

    # If the current number is not the last number, insert a multiplication sign
    # The first number must be 1
    for i in range(1, N):
        suffix[i - 1] = suffix[i - 1] * nums[i]

    # Find the max product of prefix and suffix
    max_product = prefix[-1] * suffix[0]

    # Compare the max product to the remaining products
    for i in range(N - 2):
        product = prefix[i] * suffix[i + 1]
        if product > max_product:
            max_product = product

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