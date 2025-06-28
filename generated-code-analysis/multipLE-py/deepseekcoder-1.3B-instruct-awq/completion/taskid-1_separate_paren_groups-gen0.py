from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Define a dictionary with parentheses as keys and their brackets as values
    bracket_dict = {'(': ')', '[': ']', '{': '}'}

    # Initialize the stack for parentheses
    stack = []
    result = []

    # Go through the string
    for char in paren_string:
        if char.strip() in bracket_dict:
            if stack and bracket_dict[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        elif stack:
            if bracket_dict[stack[-1]] == char:
                stack.pop()
                if not stack:
                    result.append(''.join(stack))
            else:
                stack.append(char)
        else:
            stack.append(char)

    return result
