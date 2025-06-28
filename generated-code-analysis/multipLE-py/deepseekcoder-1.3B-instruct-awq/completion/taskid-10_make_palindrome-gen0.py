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

    n = len(string)
    reverse_str = string[::-1]
    for i in range(n - 1, -1, -1):
        if string[:i] == reverse_str[:n - i]:
            return string + reverse_str[i:]
    return string + reverse_str
