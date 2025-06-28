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
    # Step 1: Build a dictionary of the encoded letters to their corresponding original letters.
    #         If a contradiction is found, or not all letters are represented in the mapping,
    #         return "Failed".
    letter_map = {}
    for i, char in enumerate(encoded):
        if char not in letter_map:
            letter_map[char] = original[i]
        elif letter_map[char] != original[i]:
            return "Failed"
    if len(letter_map) != len(set(encoded)):
        return "Failed"

    # Step 2: Map the message using the constructed dictionary.
    message_out = ""
    for char in message:
        if char in letter_map:
            message_out += letter_map[char]
        else:
            message_out += char
    return message_out
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