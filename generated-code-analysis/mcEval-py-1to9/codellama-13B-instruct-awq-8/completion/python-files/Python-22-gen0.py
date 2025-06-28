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
    
    # Map from encoded letters to their originals.
    mapping = {}
    
    # A boolean flag for the contradiction encountered during mapping construction.
    # If the flag is True, the function fails to decode the message.
    conflicted = False
    
    # Loop through all the pairs in the original-encoded pair.
    for i, (e, o) in enumerate(zip(encoded, original)):
        # If a mapping from the current encoded letter to an original letter exists,
        # check if the original letter is already mapped to another encoded letter.
        if e in mapping:
            # If a contradiction is found, set the flag to True.
            if mapping[e] != o:
                conflicted = True
                break
        # If a mapping from the current encoded letter to an original letter does not exist,
        # create the mapping.
        else:
            mapping[e] = o
    
    # If all letters are represented in the mapping, return the decoded message.
    if conflicted is False:
        decoded = ""
        for c in message:
            # If the current letter is not in the mapping, append it to the decoded message.
            if c not in mapping:
                decoded += c
            # If the current letter is in the mapping, append its original letter to the decoded message.
            else:
                decoded += mapping[c]
        
        return decoded
    # Otherwise, return "Failed".
    else:
        return "Failed"
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