from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    i = 0
    while i < len(paren_string):
        open_parens = 0
        close_parens = 0
        start_i = i
        while True:
            if paren_string[i] == '(':
                open_parens += 1
            elif paren_string[i] == ')':
                close_parens += 1

            if open_parens == close_parens:
                break

            i += 1

            if i == len(paren_string):
                break

        groups.append(paren_string[start_i:i+1])
        i += 1

    return groups
