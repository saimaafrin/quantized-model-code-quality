from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
    (None, 1)
    >>> largest_smallest_integers([])
    (None, None)
    >>> largest_smallest_integers([0])
    (None, None)
    """

    neg_int = None
    pos_int = None

    for num in lst:
        if num < 0:
            neg_int = max(neg_int, num) if neg_int is not None else num
        elif num > 0:
            pos_int = min(pos_int, num) if pos_int is not None else num

    return neg_int, pos_int
