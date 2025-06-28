from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """


    res = []
    groups = paren_string.split()

    for group in groups:
        stack = []
        max_len = 0
        for ch in group:
            if ch == '(':
                stack.append(ch)
            else:
                stack.pop()
                if len(stack) == 0:
                    max_len += 1
        res.append(max_len)

    return res
