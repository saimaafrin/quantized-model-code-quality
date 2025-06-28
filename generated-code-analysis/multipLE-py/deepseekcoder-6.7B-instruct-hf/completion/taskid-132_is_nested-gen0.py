def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """

    def bracket_validity(bracket: str) -> bool:
        stack = []
        for b in bracket:
            if b == '[':
                stack.append(b)
            else:
                if not stack:
                    return False
                stack.pop()
        return True if not stack else False

    bracket_sequence = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            bracket_sequence.append(string[i:j])

    return any(bracket_validity(bracket) for bracket in bracket_sequence)
