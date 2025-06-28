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

    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should cast the input to a list of characters,
    #   so that you can use indexing to access individual characters.
    # ------------------------------------------------------------------
    if brackets == "":
        return True
    bracket_list = list(brackets)
    stack = []
    for i in bracket_list:
        if i == "<":
            stack.append(i)
        if i == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
