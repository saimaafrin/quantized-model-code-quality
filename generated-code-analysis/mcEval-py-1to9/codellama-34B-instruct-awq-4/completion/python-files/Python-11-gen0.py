def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """

    if N == 1:
        return "1/1"

    sequence = [0, 1]

    for i in range(2, N + 1):
        sequence += [2, 1]

    sequence = sequence[:N]

    num = 1
    denom = 1
    multiplier = 1

    for i in sequence:
        if i == 0:
            num *= 2
            denom *= 2
            multiplier *= 2
        elif i == 1:
            num += multiplier
            denom += multiplier

    return f"{num}/{denom}"
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