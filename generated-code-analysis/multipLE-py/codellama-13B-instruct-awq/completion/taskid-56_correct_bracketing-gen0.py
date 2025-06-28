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


    # if brackets is empty, it is already correct
    if len(brackets) == 0:
        return True

    stack = []
    for i in range(len(brackets)):
        if brackets[i] == '<':
            stack.append('<')
        else:
            stack.pop()
            if len(stack) == 0:
                return False

    return len(stack) == 0
