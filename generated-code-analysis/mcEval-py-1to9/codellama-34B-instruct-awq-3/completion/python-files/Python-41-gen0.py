def mod_inverse(a, b):
    """
    Calculate the modular multiplicative inverse of `a` modulo `b`.
    
    This function finds an integer `x` such that (a * x) % b == 1, provided that
    `a` and `b` are coprime (i.e., gcd(a, b) == 1). It uses the Extended Euclidean
    Algorithm to compute the inverse. If `a` and `b` are not coprime, the modular
    inverse does not exist, and the function returns `None`.
    
    Args:
      a (int): The integer whose modular inverse is to be found.
      b (int): The modulus with respect to which the inverse is sought.
    
    Returns:
      int: The modular inverse of `a` modulo `b` if it exists, otherwise `None`.
    
    Examples:
      >>> mod_inverse(3, 10)
      7

      >>> mod_inverse(42, 2017)
      None
    """

    # The modular inverse of 0 is only defined if the modulus is 1.
    if a == 0:
        return 1 if b == 1 else None

    # Initialize the Extended Euclidean Algorithm.
    r_1, r_2 = b, a
    t_1, t_2 = 0, 1
    while r_2 != 0:
        quotient = r_1 // r_2
        r_1, r_2 = r_2, r_1 - quotient * r_2
        t_1, t_2 = t_2, t_1 - quotient * t_2

    # The gcd of the original inputs should be 1 if an inverse exists.
    if r_1 != 1:
        return None

    # If the result is negative, make it positive.
    if t_1 < 0:
        t_1 += b

    return t_1
def test_mod_inverse():
    test_cases = [
        (3, 10),  # Test case 1: gcd(3, 10) = 1, inverse should be 7
        (17, 3120),  # Test case 2: gcd(17, 3120) = 1, inverse should be 2753
        (42, 2017),  # Test case 3: gcd(42, 2017) = 1, inverse should be 1969
    ]
    expected_results = [
        7,  # Expected result for test case 1
        2753,  # Expected result for test case 2
        1969,  # Expected result for test case 3
    ]

    for i, (a, b) in enumerate(test_cases):
        actual_result = mod_inverse(a, b)
        expected_result = expected_results[i]
        assert actual_result == expected_result, f"Test case {i+1} failed: expected {expected_result}, got {actual_result}"
        print(f"Test case {i+1} passed: a={a}, b={b}, x0={actual_result}")

# Run the test function
test_mod_inverse()