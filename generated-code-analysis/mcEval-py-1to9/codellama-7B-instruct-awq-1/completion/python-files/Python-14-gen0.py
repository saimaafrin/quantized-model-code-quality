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
    # Check that the provided isbn is of the correct form
    isbn_parts = isbn.split('-')
    if len(isbn_parts) != 5:
        return 'Invalid'
    for part in isbn_parts[:-1]:
        if not part.isdigit():
            return 'Invalid'
    if isbn_parts[-1].isdigit():
        return 'Invalid'
    
    # Calculate the checksum
    isbn_parts = isbn.split('-')
    sum = 0
    for i, part in enumerate(isbn_parts[:-1]):
        sum += int(part) * (i % 2 + 1)
    checksum = sum % 11
    if checksum == 10:
        checksum = 'X'
    elif checksum == 11:
        return 'Invalid'
    # Format the result
    return '-'.join(isbn_parts[:-1]) + checksum
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()