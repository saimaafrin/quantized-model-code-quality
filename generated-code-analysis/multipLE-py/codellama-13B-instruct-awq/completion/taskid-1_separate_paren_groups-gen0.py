from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    start = 0
    while start < len(paren_string):
        open_braces = 0
        close_braces = 0
        for i, c in enumerate(paren_string[start:]):
            if c == '(':
                open_braces += 1
            elif c == ')':
                close_braces += 1
            if open_braces == close_braces:
                result.append(paren_string[start:start + i + 1])
                start += i + 1
                break
        else:
            raise ValueError("Invalid string passed")
    return result
