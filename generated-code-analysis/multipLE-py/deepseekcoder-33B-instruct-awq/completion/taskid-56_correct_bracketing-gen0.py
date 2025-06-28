def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('<')
    False
    >>> correct_bracketing('<>')
    True
    >>> correct_bracketing('<<><>>')
    True
    >>> correct_bracketing('><<>')
    False
    """


    brackets = list(brackets)
    bracket_stack = []
    for bracket in brackets:
        if bracket == '<':
            bracket_stack.append(bracket)
        elif bracket == '>':
            if len(bracket_stack) == 0:
                return False
            else:
                bracket_stack.pop()

    return len(bracket_stack) == 0
