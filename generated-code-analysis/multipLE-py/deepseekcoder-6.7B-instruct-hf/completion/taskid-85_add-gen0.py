from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    return sum(val for idx, val in enumerate(lst) if idx % 2 != 0 and val % 2 == 0)
