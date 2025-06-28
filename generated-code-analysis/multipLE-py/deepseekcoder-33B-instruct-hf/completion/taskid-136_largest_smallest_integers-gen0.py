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

    max_negative = None
    min_positive = None

    for num in lst:
        if num < 0:
            if max_negative is None or num > max_negative:
                max_negative = num
        elif num > 0:
            if min_positive is None or num < min_positive:
                min_positive = num

    return max_negative, min_positive
