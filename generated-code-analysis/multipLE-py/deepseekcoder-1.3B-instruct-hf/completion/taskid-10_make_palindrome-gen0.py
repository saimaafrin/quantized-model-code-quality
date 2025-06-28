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

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    n = len(string)
    rev_string = string[::-1]
    for i in range(n):
        if is_palindrome(string[i:]):
            return rev_string[:i] + string + rev_string[i:]
    return rev_string
