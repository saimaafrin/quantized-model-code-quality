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
    assert len(encoded) == len(original), "Encoded and original strings must have the same length."
    assert all(c in encoded for c in original), "Original string cannot contain characters not present in encoded string."
    if len(encoded) != len(set(encoded)):
        print("Encoded string contains duplicate letters.")
        return "Failed"
    if len(original) != len(set(original)):
        print("Original string contains duplicate letters.")
        return "Failed"
    # Build map from encoded to original letters
    mapping = {}
    for i in range(len(encoded)):
        # A letter has already been mapped
        if encoded[i] in mapping:
            print(f"Letter {encoded[i]} has already been mapped to {mapping[encoded[i]]}")
            return "Failed"
        if original[i] in mapping.values():
            print(f"Letter {original[i]} has already been mapped to {mapping[original[i]]}")
            return "Failed"
        mapping[encoded[i]] = original[i]
    # Decode
    decoded = ""
    for c in message:
        if c in mapping:
            decoded += mapping[c]
        else:
            print(f"Letter {c} not in mapping.")
            return "Failed"
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