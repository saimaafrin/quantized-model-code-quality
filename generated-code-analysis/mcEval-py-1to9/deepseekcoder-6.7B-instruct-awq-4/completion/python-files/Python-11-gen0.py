def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """
    # Determine the width of the Cantor table at the N-th level
    level = int(round(((8 * N + 1) ** 0.5 - 1) / 2))
    # Calculate the position within the current level
    pos = N - int((3 * level * level + 3 * level + 1) / 2)
    # The numerator and denominator are calculated as follows:
    num = 2 * pos + 1 if (level % 2 == 0) else -2 * pos
    den = 2 * level if (level % 2 == 0) else -2 * (level - 1)
    # Return the fraction as a string
    return f"{num}/{den}"
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