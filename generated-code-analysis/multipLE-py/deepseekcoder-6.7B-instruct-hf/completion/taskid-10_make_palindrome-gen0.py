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

    def get_prefix(string: str) -> str:
        for i in range(len(string) - 1, -1, -1):
            if string[:i] == string[len(string) - i:][::-1]:
                return string[:i]
        return ''

    prefix = get_prefix(string)
    return string + string[len(prefix):][::-1]
