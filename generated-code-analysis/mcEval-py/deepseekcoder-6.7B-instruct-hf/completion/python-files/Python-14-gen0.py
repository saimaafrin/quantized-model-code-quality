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

    # Remove any hyphens from the ISBN string
    isbn = isbn.replace("-", "")

    # Check the length of the ISBN number
    if len(isbn) != 10:
        raise ValueError("Invalid ISBN length. A valid ISBN must be 10 digits.")

    # Extract the checksum digit and the other digits
    checksum_digit = int(isbn[-1]) if isbn[-1] != 'X' else 10
    digits = [int(ch) for ch in isbn[:-1]]

    # Calculate the checksum
    checksum = sum((10 - i) * v for i, v in enumerate(digits)) % 11

    # Compare the calculated checksum with the checksum digit
    if checksum == checksum_digit:
        return "Right"
    else:
        # Calculate the correct checksum
        correct_checksum = (11 - checksum) % 11

        # Replace the incorrect checksum digit with the correct one
        isbn_list = list(isbn)
        isbn_list[-1] = str(correct_checksum) if correct_checksum != 10 else 'X'

        return "".join(isbn_list)
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()