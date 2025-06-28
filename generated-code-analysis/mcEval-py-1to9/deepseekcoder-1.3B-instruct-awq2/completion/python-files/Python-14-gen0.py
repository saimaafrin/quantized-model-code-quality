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
    if len(isbn) != 14:
        raise ValueError('ISBN must be 14 characters long')

    checksum_digit_position = 14
    isbn_chars = list(isbn)

    # Calculate the checksum
    if isbn[checksum_digit_position] in ['X', 'x']:
        isbn_chars[checksum_digit_position] = '9'
        checksum_digit_position -= 1

    # Calculate the checksum digit
    total = 0
    for index, char in enumerate(isbn_chars):
        if index % 2 == 0:
            total += int(char)
        else:
            total += int(char) * 3

    checksum_digit = (10 - (total % 10)) % 10
    isbn_chars[checksum_digit_position] = str(checksum_digit)

    return ''.join(isbn_chars) if isbn != ''.join(isbn_chars) else 'Right'
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()