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

    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']

    stack = []
    for bracket in string:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif len(stack) == 0 or closing_brackets[opening_brackets.index(stack.pop())] != bracket:
            return False
    return len(stack) == 0
