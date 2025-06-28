def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """
    def fraction_to_bin(fraction: tuple) -> str:
        """Converts a fraction to a binary string."""
        numerator, denominator = fraction
        numerator_bin = bin(numerator)[2:]
        denominator_bin = bin(denominator)[2:]
        return numerator_bin + '/' + denominator_bin

    def bin_to_fraction(binary: str) -> tuple:
        """Converts a binary string to a fraction."""
        numerator = int(binary[:len(binary)//2], 2)
        denominator = int(binary[len(binary)//2:], 2)
        return numerator, denominator

    if N == 0:
        return '0/1'
    elif N == 1:
        return '1/2'

    previous_fraction = (1, 2)
    for i in range(2, N + 1):
        previous_fraction = bin_to_fraction(fraction_to_bin((previous_fraction[0], 2 * previous_fraction[1])))

    return fraction_to_bin(previous_fraction)
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