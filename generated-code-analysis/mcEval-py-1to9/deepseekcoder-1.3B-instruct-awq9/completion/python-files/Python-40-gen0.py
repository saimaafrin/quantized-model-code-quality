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
    from string import ascii_letters as letters
    from itertools import cycle

    key = cycle(key)

    def shift_char(c, ch, lo, hi):
        """Returns the result of shifting the character c by the amount specified by
        the offset of character ch in the range lo to hi."""
        offset = letters.index(ch) - letters.index(lo)
        new_offset = (offset - offsets[letters.index(c)]) % len(offsets)
        return offsets[(letters.index(c) + new

    offsets = [0, 23, 1, 24, 2, 25, 3, 26, 4, 5, 27, 6, 28, 7, 29, 8, 20, 10, 30,
    11, 31, 12, 32, 13, 33, 14, 34, 15, 35, 16, 36, 17, 37, 18, 38, 19, 39, 20,
    40, 21, 41, 22, 42, 23, 43, 24, 44, 25, 45, 26, 46, 27, 47, 28, 48, 29, 49, 
    30, 50, 31, 51, 32, 52, 33, 53, 34, 54, 35, 55, 36, 56, 37, 57, 38, 58, 39, 59,
    40, 60, 41, 61, 42, 62, 43, 63, 44, 64, 45, 65, 46, 66, 47, 67, 48, 68, 49, 69,
    50, 70, 51, 71, 52, 72, 53, 73, 54, 74, 55, 75, 56, 76, 57, 77, 58, 78, 59, 79, 
    60, 80, 61, 81, 62, 82, 63, 83, 64, 84, 65, 85, 66, 86, 67, 87, 68, 88, 69, 89,
    70, 90, 71, 91, 72, 92, 73, 93, 74, 94, 75, 95, 76, 96,
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