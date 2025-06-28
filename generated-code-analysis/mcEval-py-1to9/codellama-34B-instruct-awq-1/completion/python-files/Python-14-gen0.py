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
    if not isbn or not isbn.isdigit():
        return "Need a valid 10-digit isbn number"

    if not isbn.isdigit() or not isbn.count("-") == 3:
        return "Need a valid 10-digit isbn number"

    isbn_numbers = isbn.split("-")

    if len(isbn_numbers) != 4:
        return "Need a valid 10-digit isbn number"

    isbn_digits = [int(digit) for digit in isbn_numbers]

    isbn_checksum = 0
    for i in range(10):
        isbn_checksum += i * isbn_digits[i]

    isbn_checksum %= 11

    if isbn_checksum == 10:
        isbn_checksum = "X"

    if isbn_checksum == isbn_digits[9]:
        return "Right"
    else:
        isbn_digits[9] = isbn_checksum
        return "-".join(str(digit) for digit in isbn_digits)
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()