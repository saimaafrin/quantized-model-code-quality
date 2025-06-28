def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """

    if N < 1:
        raise ValueError(f"N must be a positive integer (got {N}).")
    elif N > 2 ** 63 - 1:
        raise ValueError(f"N cannot be larger than 2**63 - 1 (got {N}).")

    # Initialize variables
    numerator = 1
    denominator = 1
    n = 0
    t = 1

    # Continue calculating the numerator and denominator for each term until the number is reached
    while t < N:
        numerator *= 3
        denominator *= 2
        n += 1
        t += numerator // denominator

    # Find the corresponding fraction by dividing the numerator by the denominator
    return f"{numerator // denominator}/{denominator // denominator}"
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