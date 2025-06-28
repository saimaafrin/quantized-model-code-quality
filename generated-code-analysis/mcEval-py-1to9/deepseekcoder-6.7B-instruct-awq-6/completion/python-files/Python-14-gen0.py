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

    # Remove the hyphen and convert the last character to a digit if it's not
    # 'X' or 'x', then split the string into a list of characters
    isbn_list = [char for char in list(isbn.replace("-", "")[:-1]) + [isbn[-1]]]
    
    # Convert characters to integers, calculate the checksum
    checksum = sum((10 - i) * int(x) for i, x in enumerate(isbn_list)) % 11

    # Check if the calculated checksum matches the provided checksum
    if checksum == (10 if isbn_list[-1] in {"X", "x"} else int(isbn_list[-1])):
        return "Right"
    else:
        # If the checksum is incorrect, correct it by changing the last character
        # to the correct checksum digit
        correct_checksum = (11 - checksum) % 11
        correct_checksum = "X" if correct_checksum == 10 else str(correct_checksum)
        isbn_list[-1] = correct_checksum
        return "".join(isbn_list[:-1]) + "-" + isbn_list[-1]
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()