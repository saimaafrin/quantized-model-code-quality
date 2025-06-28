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

    rotated_alphabet = {
        "a": "k",
        "b": "l",
        "c": "m",
        "d": "n",
        "e": "o",
        "f": "p",
        "g": "q",
        "h": "r",
        "i": "s",
        "j": "t",
        "k": "u",
        "l": "v",
        "m": "w",
        "n": "x",
        "o": "y",
        "p": "z",
        "q": "a",
        "r": "b",
        "s": "c",
        "t": "d",
        "u": "e",
        "v": "f",
        "w": "g",
        "x": "h",
        "y": "i",
        "z": "j",
    }

    encrypted_string = ""
    for char in s:
        if char.isalpha():
            encrypted_string += rotated_alphabet.get(char.lower())
        else:
            encrypted_string += char

    return encrypted_string
