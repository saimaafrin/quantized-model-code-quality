def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """

    # The first numerator in the Cantor table is 1/3.
    numerator = 1

    # The first denominator in the Cantor table is 3.
    denominator = 3

    # The first fraction in the Cantor table is 1/3.
    fraction = f"{numerator}/{denominator}"

    # While the position in the Cantor table is less than the argument N...
    while N > 1:

        # If the position is odd, the numerator is increased by the current denominator.
        if N % 2:
            numerator += denominator

        # If the position is even, the denominator is doubled.
        else:
            denominator *= 2

        # The fraction is recalculated.
        fraction = f"{numerator}/{denominator}"

        # The position in the Cantor table is reduced by 1.
        N -= 1

    return fraction
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