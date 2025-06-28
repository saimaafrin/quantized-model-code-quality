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

    string = string.strip().lower()
    if not string:
        return ''

    # find the first letter that is not a palindrome
    start = 0
    while start < len(string) - 1 and string[start] == string[-1 - start]:
        start += 1

    # append a reversed prefix to the end
    return string + string[start: len(string) - 1 - start : -1]
