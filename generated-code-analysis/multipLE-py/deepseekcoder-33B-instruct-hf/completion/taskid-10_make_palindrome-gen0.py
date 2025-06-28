def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """

    str_len = len(string)
    if str_len < 2:
        return string
    rev_string = string[::-1]
    for i in range(str_len):
        if string.startswith(rev_string[i:]):
            return string + rev_string[str_len - i : str_len]
    return string + rev_string
