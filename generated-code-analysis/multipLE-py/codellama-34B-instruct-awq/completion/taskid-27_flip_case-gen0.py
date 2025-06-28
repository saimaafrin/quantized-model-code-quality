def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped_chars = []
    for char in string:
        if char.islower():
            flipped_chars.append(char.upper())
        else:
            flipped_chars.append(char.lower())
    return ''.join(flipped_chars)
