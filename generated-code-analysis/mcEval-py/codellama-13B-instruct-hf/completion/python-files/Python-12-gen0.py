def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """

    # Use a dynamic programming solution to determine the maximum product that can be obtained by inserting K multiplication signs into the number string.

    # Example 1
    # num_str = '3'
    # N = 1
    # K = 0
    # Expected output = 3

    # Example 2
    # num_str = '23'
    # N = 2
    # K = 1
    # Expected output = 51

    # Example 3
    # num_str = '23'
    # N = 2
    # K = 2
    # Expected output = 46

    # Example 4
    # num_str = '1000'
    # N = 4
    # K = 1
    # Expected output = 2000

    # Example 5
    # num_str = '999'
    # N = 3
    # K = 2
    # Expected output = 9801

    # Example 6
    # num_str = '1'
    # N = 1
    # K = 0
    # Expected output = 1

    # Initialize variables.
    num_arr = list(map(int, num_str))

    # Base case: If there are no multiplication signs to insert, return the number string.
    if K == 0:
        return int("".join(map(str, num_arr)))

    # Base case: If there are no elements in the number string, return 0.
    if N == 0:
        return 0

    # Initialize a list to store the maximum products for each subproblem.
    max_product_arr = [0 for _ in range(N)]

    # Loop through each subproblem in the number string.
    for i in range(N):
        # Initialize a variable to store the current maximum product.
        current_max_product = 0

        # Initialize a variable to store the current number.
        current_num = num_arr[i]

        # Base case: If the current subproblem is the first subproblem, set the current maximum product to the current number.
        if i == 0:
            current_max_product = current_num

        # Base case: If the current subproblem is the last subproblem, set the current maximum product to the current number multiplied by the previous subproblem's maximum product.
        if i == N - 1:
            current_max_product = current_num * max_product_arr[i - 1]

        # If the current subproblem is neither the first nor the last subproblem, set the current maximum product to the current number multiplied by the previous subproblem's maximum product and the current subproblem's maximum product.
        if 0 < i < N - 1:
            current_max_product = current_num * max_product_arr[i - 1] * num_arr[i + 1]

        # Store the current maximum product in the maximum products list.
        max_product_arr[i] = current_max_product

    # Return the maximum product that can be obtained by inserting K multiplication signs into the number string.
    return max_product_arr[N - 1]
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