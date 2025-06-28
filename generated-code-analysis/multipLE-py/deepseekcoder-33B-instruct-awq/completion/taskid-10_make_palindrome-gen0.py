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


    string_length = len(string)

    if string_length == 0:
        return ''

    string_rev = string[::-1]

    for i in range(string_length):
        if string[:(string_length - i)] == string_rev[i:]:
            return string + string_rev[string_length - i:]

    return string + string_rev
