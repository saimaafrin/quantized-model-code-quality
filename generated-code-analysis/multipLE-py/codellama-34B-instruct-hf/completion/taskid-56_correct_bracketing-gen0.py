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

    left_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            left_brackets += 1
        elif bracket == ">":
            if left_brackets == 0:
                return False
            else:
                left_brackets -= 1

    if left_brackets == 0:
        return True
    else:
        return False
