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

    # This function is supposed to return True if every opening bracket has a corresponding closing bracket.
    # The brackets are represented as a string of "<" and ">".
    # We can solve this problem by using a stack data structure.
    # We iterate through the string, pushing every "<" onto the stack and every ">" we see we pop off the top of the stack.
    # If at any point we try to pop an empty stack, we return False because we have a closing bracket without a matching opening bracket.
    # If we get through the entire string without any issues, we return True because every opening bracket has a corresponding closing bracket.

    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
