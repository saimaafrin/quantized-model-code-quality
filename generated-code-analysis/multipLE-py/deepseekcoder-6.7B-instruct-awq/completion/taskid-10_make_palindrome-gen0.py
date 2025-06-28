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

    if not string:
        return ''
    # Determine longest postfix that is a palindrome
    for i in range(len(string), -1, -1):
        if string[:i] == string[i-1::-1]:
            break
    # Return palindrome by appending reversed prefix
    return string + string[i-1::-1]
