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
    # Create a dictionary that maps encoded letters to their corresponding original letters
    encoded_original_dict = {}
    
    # Iterate through each letter in the encoded string
    for i in range(len(encoded)):
        # If the encoded letter is not in the dictionary yet, add it
        if encoded[i] not in encoded_original_dict:
            encoded_original_dict[encoded[i]] = original[i]
        # If the encoded letter is already in the dictionary, check if it maps to the same original letter
        elif encoded_original_dict[encoded[i]] != original[i]:
            # If it doesn't, the decoding is not possible and the function returns "Failed"
            return "Failed"
    
    # If not all letters in the original string are represented in the dictionary, the decoding is not possible
    # and the function returns "Failed"
    for i in range(len(original)):
        if original[i] not in encoded_original_dict:
            return "Failed"
    
    # Construct the decoded message by using the mapping of encoded letters to their corresponding original letters
    decoded = ""
    for letter in message:
        if letter not in encoded_original_dict:
            decoded += letter
        else:
            decoded += encoded_original_dict[letter]
    
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