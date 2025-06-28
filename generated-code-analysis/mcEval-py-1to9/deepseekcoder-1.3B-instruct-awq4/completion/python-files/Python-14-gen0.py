def verify_isbn(isbn: str) -> str:
    """
    Verify the correctness of a given ISBN number and correct it if necessary.

    The function checks the provided ISBN number against the ISBN standard checksum calculation.
    If the checksum is correct, the function returns "Right". If the checksum is incorrect,
    the function returns the corrected ISBN number.

    Args:
    isbn: A string representing the ISBN number to be verified. The format should be 'x-xxx-xxxxx-x',
          where 'x' is a digit, and the last 'x' could also be 'X' representing the checksum digit.

    Returns:
    A string that is either "Right" if the ISBN checksum is correct, or the corrected ISBN number
    in the same format as the input if the checksum is incorrect.

    Examples:
    >>> verify_isbn("0-670-82162-4")
    'Right'
    
    >>> verify_isbn("0-670-82162-0")
    '0-670-82162-4'
    """
    # check format
    if len(isbn) != 14 or isbn[:2] != '0-' or not isbn[2:-1].isdigit() or isbn[-1] not in '0-X':
        return 'Invalid ISBN'

    # calculate checksum
    weights = [1, 3] * 5
    digits = isbn[:-1]
    checksum = isbn[-1].lower()

    if checksum == 'x':
        checksum = '10'

    total = sum(d * w for d, w in zip(digits, weights)) + int(checksum)
    total = 10 - (total % 10)
    total = str(total)

    return total
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()