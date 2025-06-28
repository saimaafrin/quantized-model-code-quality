def decode(encoded: str, original: str, message: str) -> str:
    """
    Decodes an encrypted message using a cipher derived from a known encoded-original pair.
    
    The function builds a mapping from encoded letters to their original letters and uses this
    mapping to decode a given encrypted message. If a contradiction is found during mapping
    construction, or not all letters are represented in the mapping, the function returns "Failed".
    
    Args:
    encoded (str): A string representing the encoded information.
    original (str): A string representing the original information corresponding to the encoded string.
    message (str): A string representing the encrypted message to be decoded.
    
    Returns:
    str: The decoded message if successful, or "Failed" if the decoding is not possible.
    
    Examples:
    >>> decode("AA", "AB", "EOWIE")
    'Failed'    
    >>> decode("MSRTZCJKPFLQYVAWBINXUEDGHOOILSMIJFRCOPPQCEUNYDUMPP", "YIZSDWAHLNOVFUCERKJXQMGTBPPKOIYKANZWPLLVWMQJFGQYLL", "FLSO")
    'NOIP'
    """

    assert isinstance(encoded, str)
    assert isinstance(original, str)
    assert isinstance(message, str)

    # Convert all strings to lowercase for consistency
    encoded = encoded.lower()
    original = original.lower()
    message = message.lower()

    # Initialize the mapping from encoded letters to original letters
    enc_to_orig = {}

    # Iterate over the encoded string and original string simultaneously
    for i in range(len(encoded)):
        enc_char = encoded[i]
        orig_char = original[i]
        if enc_char in enc_to_orig:
            if enc_to_orig[enc_char] != orig_char:
                return "Failed"
        else:
            enc_to_orig[enc_char] = orig_char

    # Verify that all letters are represented in the mapping
    if len(enc_to_orig) != 26:
        return "Failed"

    # Initialize the decoded message
    decoded = ""

    # Iterate over the encrypted message
    for c in message:
        if c in enc_to_orig:
            decoded += enc_to_orig[c]
        else:
            decoded += c

    return decoded
def test_decode():
    # Test case 1: Contradiction in mapping
    assert decode("AA", "AB", "EOWIE") == "Failed", "Test case 1 failed"

    # Test case 2: Not all letters are represented
    assert decode("QWERTYUIOPLKJHGFDSAZXCVBN", "ABCDEFGHIJKLMNOPQRSTUVWXY", "DSLIEWO") == "Failed", "Test case 2 failed"

    # Test case 3: Successful decoding
    assert decode("MSRTZCJKPFLQYVAWBINXUEDGHOOILSMIJFRCOPPQCEUNYDUMPP", "YIZSDWAHLNOVFUCERKJXQMGTBPPKOIYKANZWPLLVWMQJFGQYLL", "FLSO") == "NOIP", "Test case 3 failed"
    
    # Test case 4: Character in message not in mapping
    assert decode("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ", "UVWXYZ") == "Failed", "Test case 4 failed"

    # Test case 5: Empty strings
    assert decode("", "", "") == "Failed", "Test case 5 failed"

    print("All test cases passed!")

# Call the test function to run the test cases
test_decode()