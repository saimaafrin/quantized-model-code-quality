def solve(s: str) -> str:
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    >>> solve('1234')
    '4321'
    >>> solve('ab')
    'AB'
    >>> solve('#a@C')
    '#A@c'
    """


    # your code here
    reversed_string = s[::-1]
    result = ""

    if not any(char.isalpha() for char in reversed_string):
        return reversed_string
    else:
        for character in reversed_string:
            if character.isupper():
                result += character.lower()
            elif character.islower():
                result += character.upper()
            else:
                result += character
        return result
