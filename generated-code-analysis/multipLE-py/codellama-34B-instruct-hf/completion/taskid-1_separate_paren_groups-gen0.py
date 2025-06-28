from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Implement your solution below
    paren_list = []
    curr_paren_group = ""
    curr_num_parens = 0
    for char in paren_string:
        if char == "(":
            curr_num_parens += 1
            curr_paren_group += char
        elif char == ")":
            curr_num_parens -= 1
            curr_paren_group += char
        if curr_num_parens == 0:
            paren_list.append(curr_paren_group)
            curr_paren_group = ""
    return paren_list
