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
    # Check if the original string and the encoded string have the same length.
    if len(original) != len(encoded):
        return "Failed"
    
    # Create a dictionary mapping each encoded letter to its original letter.
    mapping = {}
    for i in range(len(original)):
        # Check if the mapping is not already defined for the current encoded letter.
        if encoded[i] not in mapping:
            # Check if the mapping is not already defined for the current original letter.
            if original[i] not in mapping.values():
                mapping[encoded[i]] = original[i]
            # If the mapping is already defined for the current original letter, fail.
            else:
                return "Failed"
        # If the mapping is already defined for the current encoded letter, fail.
        else:
            return "Failed"
    
    # Check if all letters from the original string are represented in the mapping.
    for i in range(len(original)):
        if original[i] not in mapping.values():
            return "Failed"
    
    # Check if the length of the decoded message is equal to the length of the original string.
    if len(message) != len(original):
        return "Failed"
    
    # Create the decoded message by applying the mapping to each encoded letter.
    decoded = ""
    for i in range(len(message)):
        decoded += mapping[message[i]]
    
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