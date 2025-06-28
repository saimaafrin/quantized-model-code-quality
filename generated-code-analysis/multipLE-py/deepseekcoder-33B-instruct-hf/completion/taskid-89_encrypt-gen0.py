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

    res = ""
    for i in s:
        if i.isalpha():
            shift = 4
            char = chr(((ord(i) - 97 + shift) % 26) + 97) if i.islower() else chr(((ord(i) - 65 + shift) % 26) + 65)
            res += char
        else:
            res += i
    return res
