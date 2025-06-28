def max_product(num_str: str, N: int, K: int) -> int:
    """
    Function name: max_product
    Arguments:
    num_str (str): A string representing the number string.
    N (int): An integer representing the length of the number string.
    K (int): An integer representing the number of multiplication signs to insert.
    Return type: int (The function returns the maximum product that can be obtained by inserting Kmultiplication signs into the number string.)
    """
    # Converts the number string to a list of integers.
    num = [int(i) for i in num_str]
    # Creates a list to store the product of each slice.
    product = []
    # Iterates over the length of the number string.
    for i in range(len(num)):
        # Calculates the product of the slice of the number string.
        product.append(num[i] * num[(i + 1) % len(num)])
    # Converts the list of products to a tuple.
    product = tuple(product)
    # Creates a list to store the index of each product.
    index = []
    # Iterates over the length of the number string.
    for i in range(len(num)):
        # Calculates the index of each product.
        index.append(i)
    # Converts the list of indices to a tuple.
    index = tuple(index)
    # Sorts the product list in descending order.
    product = sorted(product, reverse=True)
    # Creates a list to store the index of each sorted product.
    sort_index = []
    # Iterates over the length of the number string.
    for i in range(len(product)):
        # Calculates the index of each sorted product.
        sort_index.append(index[product[i]-1])
    # Converts the list of indices to a tuple.
    sort_index = tuple(sort_index)
    # Creates a list to store the multiplication signs.
    mult = []
    # Iterates over the length of the number string.
    for i in range(N-1):
        # Calculates the multiplication signs.
        mult.append("*")
    # Converts the list of multiplication signs to a string.
    mult = "".join(mult)
    # Creates a list to store the position of each multiplication sign.
    mult_pos = []
    # Iterates over the length of the number string.
    for i in range(N-1):
        # Calculates the position of each multiplication sign.
        mult_pos.append(sort_index[i] + 1)
    # Converts the list of positions to a tuple.
    mult_pos = tuple(mult_pos)
    # Calculates the number of multiplication signs to be inserted.
    mult_num = K - (N-1)
    # Creates a list to store the indices of each multiplication sign to be inserted.
    mult_index = []
    # Iterates over the length of the number string.
    for i in range(mult_num):
        # Calculates the indices of each multiplication sign to be inserted.
        mult_index.append(mult_pos[i] + i)
    # Converts the list of indices to a tuple.
    mult_index = tuple(mult_index)
    # Creates a list to store the multiplication signs to be inserted.
    mult_insert = []
    # Iterates over the length of the number string.
    for i in range(mult_num):
        # Calculates the multiplication signs to be inserted.
        mult_insert.append("*")
    # Converts the list of multiplication signs to a string.
    mult_insert = "".join(mult_insert)
    # Inserts the multiplication signs into the number string.
    num_insert = mult_insert.join(num_str)
    # Calculates the maximum product that can be obtained by inserting K multiplication signs into the number string.
    product = eval(num_insert)
    return product
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