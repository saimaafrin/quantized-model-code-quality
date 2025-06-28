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

    alpha = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for i in range(len(s)):
        if s[i].isalpha():
            s = s[:i] + s[i].upper() + s[i + 1 :]
    if len(s) == 0:
        return s
    return s[::-1]
