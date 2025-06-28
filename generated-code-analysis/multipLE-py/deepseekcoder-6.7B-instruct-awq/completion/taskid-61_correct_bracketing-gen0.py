def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('(')
    False
    >>> correct_bracketing('()')
    True
    >>> correct_bracketing('(()())')
    True
    >>> correct_bracketing(')(()')
    False
    """

    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if not stack:  # there is no corresponding opening bracket
                return False
            stack.pop()  # we remove the last opening bracket
    return not stack  # if there are any unmatched opening brackets, return False
