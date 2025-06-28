def vigenere_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts a ciphertext encrypted with the Vigenère cipher using the provided key.
    
    The Vigenère cipher is a method of encrypting alphabetic text by using a series of
    Caesar ciphers based on the letters of a keyword. This function reverses the process
    to recover the original plaintext from the ciphertext.

    Args:
        key (str): The encryption key used to encrypt the original plaintext.
                   This key should consist only of alphabetic characters.
        ciphertext (str): The encrypted text that needs to be decrypted.
                          The ciphertext should consist only of alphabetic characters.

    Returns:
        str: The decrypted plaintext corresponding to the input ciphertext.

    Examples:
        >>> vigenere_decrypt("CompleteVictory", "Yvqgpxaimmklongnzfwpvxmniytm")
        'Wherethereisawillthereisaway'

        >>> vigenere_decrypt("ABC", "DEF")
        'DCB'
    """
    # 1. Declare variables for the key, ciphertext, and output.
    #    In the case of the ciphertext, we use a list to store the characters
    #    of the ciphertext.
    key_list = []
    ciphertext_list = []
    plaintext = ""

    # 2. Convert the input key and ciphertext into lists of characters.
    for char in key:
        key_list.append(char)
    for char in ciphertext:
        ciphertext_list.append(char)

    # 3. Loop through the characters of the ciphertext, decrypting each one
    #    using the corresponding character of the key.
    for i in range(len(ciphertext_list)):
        # a. Calculate the offset from the ASCII value of the character
        #    in the ciphertext using the ASCII value of the character in
        #    the key.
        offset = ord(key_list[i % len(key_list)]) - 97
        # b. Subtract the offset from the ASCII value of the character in
        #    the ciphertext to get the new ASCII value.
        new_ascii_value = ord(ciphertext_list[i]) - offset
        # c. Convert the new ASCII value back into a character.
        plaintext += chr(new_ascii_value)

    # 4. Return the decrypted plaintext.
    return plaintext
def test_vigenere_decrypt():
    # Test case 1: Example provided in the problem statement
    key1 = "CompleteVictory"
    ciphertext1 = "Yvqgpxaimmklongnzfwpvxmniytm"
    expected_plaintext1 = "Wherethereisawillthereisaway"
    assert vigenere_decrypt(key1, ciphertext1) == expected_plaintext1, "Test case 1 failed"

    # Test case 2: All uppercase characters
    key2 = "ABC"
    ciphertext2 = "DEF"
    expected_plaintext2 = "DDD"
    assert vigenere_decrypt(key2, ciphertext2) == expected_plaintext2, "Test case 2 failed"

    # Test case 3: All lowercase characters
    key3 = "xyz"
    ciphertext3 = "abc"
    expected_plaintext3 = "ddd"
    assert vigenere_decrypt(key3, ciphertext3) == expected_plaintext3, "Test case 3 failed"

    # Test case 4: Mixed case characters
    key4 = "MiXeD"
    ciphertext4 = "JpOeR"
    expected_plaintext4 = "XhRaO"
    assert vigenere_decrypt(key4, ciphertext4) == expected_plaintext4, "Test case 4 failed"

    # Test case 5: Key shorter than ciphertext
    key5 = "short"
    ciphertext5 = "PqrsPqrsPq"
    expected_plaintext5 = "XjdbWykeYx"
    assert vigenere_decrypt(key5, ciphertext5) == expected_plaintext5, "Test case 5 failed"

    print("All test cases passed!")

# Run the test function
test_vigenere_decrypt()