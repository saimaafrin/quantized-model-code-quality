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

    opening = 0
    closing = 0
    for char in brackets:
        if char == '<':
            opening += 1
        else:
            closing += 1

        if closing > opening:
            return False

    return closing == opening
