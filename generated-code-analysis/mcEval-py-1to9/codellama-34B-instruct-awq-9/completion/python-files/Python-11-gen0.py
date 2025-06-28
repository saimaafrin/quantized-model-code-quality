def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """
    # Initialize the numerator and denominator to 1.
    numerator = 1
    denominator = 1

    # Loop while the numerator is less than or equal to the denominator.
    while numerator <= denominator:
        # Check if the position is even.
        if N % 2 == 0:
            # If the position is even, the numerator must be even.
            numerator = numerator * 2
        else:
            # If the position is odd, the denominator must be even.
            denominator = denominator * 2

        # The position must be divided by 2.
        N = N // 2

    # Return the fraction at the position in the Cantor table.
    return f"{numerator}/{denominator}"
def test_cantor_numbering():
    # Test case 1: N = 1, the first element, should be "1/1"
    assert cantor_numbering(1)=="1/1"

    # Test case 2: N = 2, the second element, should be "1/2"
    assert cantor_numbering(2)=="1/2"

    # Test case 3: N = 6, the sixth element, should be "1/3"
    assert cantor_numbering(6)=="1/3"

    # Corrected test case: N = 7, the seventh element, should be "1/4"
    assert cantor_numbering(7) == "1/4"

    # Additional test case: N = 8, the eighth element, should be "2/3"
    assert cantor_numbering(8) == "2/3"


test_cantor_numbering()