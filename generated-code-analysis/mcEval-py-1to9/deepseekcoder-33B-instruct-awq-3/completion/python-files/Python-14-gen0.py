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
    isbn_list = list(isbn.replace('-', ''))

    # Compute the checksum
    checksum = sum((10 - i) * (int(x) if x.isdigit() else 10) for i, x in enumerate(isbn_list))
    checksum %= 11

    # Determine the expected checksum digit
    checksum_digit = 'X' if checksum == 10 else str(checksum)

    # Determine whether the ISBN is correct
    if isbn_list[-1] == checksum_digit:
        return 'Right'
    else:
        # Replace the last digit with the correct checksum digit
        isbn_list[-1] = checksum_digit

        # Format the corrected ISBN and return it
        corrected_isbn = '-'.join(isbn_list)
        return corrected_isbn
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()