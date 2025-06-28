def encrypt(s: str) -> str:
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """

    encrypted = ""
    for c in s:
        if c.isalpha():
            shift = 2 * 2 if c.islower() else 2 * 2
            start = ord('a') if c.islower() else ord('A')
            encrypted += chr((ord(c) - start + 2) % 26 + start)
        else:
            encrypted += c
    return encrypted
